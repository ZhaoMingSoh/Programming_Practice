# Description of the problem : The function should return an array containing any combination of elements that add up to exactly the targetSum.

# Default Method :
def howSum_Default(targetnum : int, numbers : list[int]):
    sum_comb = []
    # base case 1) when targetnum is deducted until 0, then return []
    if targetnum == 0:
        return sum_comb

    if targetnum < 0:
        return None
    
    for num in numbers:
        diff = targetnum - num
        temp = howSum_Default(diff,numbers)
        if temp != None:
            sum_comb = list(temp)
            sum_comb.append(num)
            return sum_comb

    return None

# Method 1 : Top-down approach (memoisation)
def howSum(targetnum : int, numbers : list[int], memo = None):
    # print(memo)
    sum_comb = []
    if memo == None:
        memo = {}

    if targetnum in memo:
        return memo[targetnum]
    
    # base case 1) when targetnum is deducted until 0, then return []
    if targetnum == 0:
        return sum_comb

    if targetnum < 0:
        return None

    for num in numbers:
        diff = targetnum - num
        # 2) when the targetnum gets deducted to 0, the iteration in which the targetnum == 0 will return an empty sun_comb={}, 
        temp = howSum(diff, numbers, memo)
        if  temp != None:
            sum_comb = list(temp)
            sum_comb.append(num) # store the edge value along the branches of the tree that leads the targetnum to be 0.
            memo[targetnum] = sum_comb
            return sum_comb

    memo[targetnum] = None
    return None

def howSum_Tabulation(targetNum : int, numbers : list[int]):
    # Table of size targetNum+1 as the index refers to all the possible values that can sum to the targetNum.
    table = [None] * (targetNum+1)
    # Seed value -> empty list as it indicates base case for when a possible combination is found
    table[0] = []

    # For each index of the table, increment it by each number from numbers, then copy the list from the initial index, then appending the num alongside it.
    for pos in range(targetNum):
        if table[pos] != None: # Only look ahead if it has a list in it.
            for num in numbers:
                index_ahead = pos + num # increment it by each number from numbers
                if index_ahead <= targetNum:
                    temp = list(table[pos]) # then copy the list from the initial index
                    temp.append(num) # appending the num alongside it
                    table[index_ahead] = temp
    
    return table[targetNum]

# m = targetsum
# n = numbers.length

# Brute Force:
# time : O(n^m*m) --> account for the array making (worst case the result array is length m)
# space : O(m)

# Memoised:
# time : O(n*m*m)
# space : O(m*m) --> comes from the memo={} (worst case each key has the result array of length m)

if __name__ == "__main__":
    print(f"The combination for the targetsum = {7} is {howSum(7,[2,3])}")
    print(f"The combination for the targetsum = {7} is {howSum(7,[5,3,4,7])}")
    print(f"The combination for the targetsum = {7} is {howSum_Default(7,[5,3,4,7])}")
    print(f"(Tabulation) The combination for the targetsum = {7} is {howSum_Tabulation(7,[5,3,4,7])}")
    print(f"(Tabulation) The combination for the targetsum = {7} is {howSum_Tabulation(7,[5,3,4])}")
    print(f"The combination for the targetsum = {8} is {howSum(8,[2,3,5])}")
    print(f"(Tabulation) The combination for the targetsum = {8} is {howSum_Tabulation(8,[2,3,5])}")
    print(f"The combination for the targetsum = {300} is {howSum(300,[7,14])}")
    print(f"(Tabulation) The combination for the targetsum = {300} is {howSum_Tabulation(300,[7,14])}")


