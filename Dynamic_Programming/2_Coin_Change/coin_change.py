import math
from turtle import forward

# Method 1 : DP (Top-down approach - Memoisation)
def coinChange_list(coins: list[int], amount: int, memo = None) -> list:
    sum_comb = []
    # table to store all the repeated subtree solutions
    if memo == None:
        memo = {}
    # Look up the solution of the repeated subtree
    if amount in memo:
        return memo[amount]

    # Base Case
    if amount == 0:
        return sum_comb
    if amount < 0:
        return None

    # Record the smallest combination for each deduced amount starting from the top.
    smallest_comb = None

    # Deduct the amount with each coin, take the difference and put it into a recursive function call until the amount reaches 0 (base case).
    for coin in coins:
        diff = amount - coin
        temp = coinChange_list(coins,diff,memo)
        if temp != None:
            sum_comb = list(temp)
            sum_comb.append(coin)
            if smallest_comb == None or len(sum_comb) < len(smallest_comb):
                smallest_comb = list(sum_comb)
    
    memo[amount] = smallest_comb
    return smallest_comb

def coinChange_Int(coins: list[int], amount: int, memo = None) -> int:
    if memo == None:
        memo = {}
    
    if amount in memo:
        return memo[amount]

    # Base case
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    smallest_comb = math.inf # initiate this as the largest value

    for coin in coins:
        diff = amount - coin
        temp = coinChange_Int(coins,diff,memo)
        if temp >= 0 and temp < smallest_comb: # This prevent -1 value from ever returning, only the base case(0) + the rest of the parents preceding the base case
            smallest_comb = temp + 1 # for example, 4 (-1) -> 3 (-1) -> 2 (-1) -> 1 (-1) -> 0 (return 0)

    if smallest_comb == math.inf: # deal with the case where there is no combination of coins possible for the amount.
        return -1

    memo[amount] = smallest_comb
    return memo[amount]
            
def coinChange_Tabulation(coins: list[int], amount: int):
    # Table of size amount + 1 with -1 as value
    table = [-1]*(amount+1)
    # Seed value -> when amount == 0 return 0
    table[0] = 0

    # Find the minimum comb for every single amount indicated as index of the table
    for index in range(amount+1):
        # Only proceed with the particular index if it is reachable from the addition of the coins
        if table[index] >= 0:
            for coin in coins:
                index_forward = index + coin # look at the addition of the current index + coin
                if index_forward <= amount: # ensure it does not go over the boundary of the table
                    temp = table[index] + 1
                    if table[index_forward] == -1 or temp < table[index_forward]: # check if the index + coin is either still -1 (have not been assigned but is reachable) or that we found a smaller amount than it has currently
                        table[index_forward] = temp
    
    return table[amount]

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    print("coinChange_list")
    print(f"The amount of coins needed for {11} is {coinChange_list(coins,amount)}")
    print(f"The amount of coins needed for {100} is {coinChange_list(coins,100)}")
    print(f"The amount of coins needed for {4} is {coinChange_list([1,2],4)}")
    print(f"The amount of coins needed for {3} is {coinChange_list([2],3)}")
    print(f"The amount of coins needed for {0} is {coinChange_list([1],0)}")

    print("coinChange_Int")
    print(f"The amount of coins needed for {11} is {coinChange_Int(coins,amount)}")
    print(f"The amount of coins needed for {100} is {coinChange_Int(coins,100)}")
    print(f"The amount of coins needed for {4} is {coinChange_Int([1,2],4)}")
    print(f"The amount of coins needed for {3} is {coinChange_Int([2],3)}")
    print(f"The amount of coins needed for {0} is {coinChange_Int([1],0)}")

    print("coinChange_Tabulation")
    print(f"The amount of coins needed for {11} is {coinChange_Tabulation(coins,amount)}")
    print(f"The amount of coins needed for {100} is {coinChange_Tabulation(coins,100)}")
    print(f"The amount of coins needed for {4} is {coinChange_Tabulation([1,2],4)}")
    print(f"The amount of coins needed for {3} is {coinChange_Tabulation([2],3)}")
    print(f"The amount of coins needed for {0} is {coinChange_Tabulation([1],0)}")
