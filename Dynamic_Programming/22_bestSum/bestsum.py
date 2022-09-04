# Default Method :
def bestSum_Default(targetsum : int, numbers : list[int]):
    sum_comb = []

    # base case
    if targetsum == 0:
        return sum_comb

    if targetsum < 0:
        return None

    shortestcombination = None # This variable will keep track of every single combination of elements that sum up to the root value on every single subtrees

    for num in numbers:
        diff = targetsum - num
        temp = bestSum_Default(diff, numbers)
        if temp != None:
            sum_comb = list(temp)
            sum_comb.append(num)
            if shortestcombination == None or len(sum_comb) < len(shortestcombination):
                shortestcombination = list(sum_comb)

    return shortestcombination

# Method 1 : Top-down memoisation
def bestSum(targetsum : int, numbers : list[int], memo = None):
    sum_comb = []
    if memo == None:
        memo = {}
    
    if targetsum in memo:
        return memo[targetsum]

    if targetsum == 0:
        return sum_comb

    if targetsum < 0:
        return None

    shortestcombination = None # This variable will keep track of every single combination of elements that sum up to the root value on every single subtrees
    
    for num in numbers:
        diff = targetsum - num
        temp = bestSum(diff, numbers, memo)
        # When a summation is found, append the edge value that made it 0.
        if temp != None:
            sum_comb = list(temp)
            sum_comb.append(num)
            # We check if the current comb of elements that summed up to the current root value is smaller than the previous branch.
            if shortestcombination == None or len(sum_comb) < len(shortestcombination):
                shortestcombination = list(sum_comb)

    memo[targetsum] = shortestcombination
    return shortestcombination

def bestSum_Tabulation(targetsum : int, numbers : list[int]):
    # Table of size targetsum + 1
    table = [None] * (targetsum + 1)
    # Seed value -> the base case is when targetnum = 0 then return an array of empty list [].
    table[0] = []

    for index in range(targetsum):
        if table[index] != None:
            for num in numbers:
                index_forward = index + num
                combination = list(table[index]) # Take the current index list and add on the num to it
                combination.append(num)
                if index_forward <= targetsum:
                    # Take the combination list and compare with the already existing list in the index + num position.
                    if table[index_forward] == None or len(table[index_forward]) > len(combination):
                        table[index_forward] = combination
                    
    return table[targetsum]

# Brute Force
# Time : O(n^m * m) -> height of tree is m and the branching factor is n and each level of the tree may have an array of size m
# Space : O(m^2) -> each level of the call stack may have an array of size m as the shortestcombination

# Memoisation
# Time : O(n*m^2) -> height of the tree is m and no branching factor
# Space : O(m^2) -> same as the brute force

# Tabulation
# Time : O(m^2*n) -> 
# Space : 

if __name__ == "__main__":
    print(f"(Memoisation) The smallest combination of elements from {[5,3,4,7]} that sums up to {7} is {bestSum_Default(7,[5,3,4,7])}")
    print(f"(Tabulation) The smallest combination of elements from {[5,3,4,7]} that sums up to {7} is {bestSum_Tabulation(7,[5,3,4,7])}")
    print(f"(Default) The smallest combination of elements from {[5,3,4,7]} that sums up to {7} is {bestSum_Default(7,[5,3,4,7])}")
    print(f"(Memoisation) The smallest combination of elements from {[2,3,5]} that sums up to {8} is {bestSum(8,[2,3,5])}")
    print(f"(Tabulation) The smallest combination of elements from {[2,3,5]} that sums up to {8} is {bestSum_Tabulation(8,[2,3,5])}")
    print(f"(Memoisation) The smallest combination of elements from {[1,4,5]}that sums up to {8} is {bestSum(8,[1,4,5])}")
    print(f"(Tabulation) The smallest combination of elements from {[1,4,5]}that sums up to {8} is {bestSum_Tabulation(8,[1,4,5])}")
    print(f"(Memoisation) The smallest combination of elements from {[1,2,5,25]} that sums up to {100} is {bestSum(100,[1,2,5,25])}")
    print(f"(Tabulation) The smallest combination of elements from {[1,2,5,25]} that sums up to {100} is {bestSum_Tabulation(100,[1,2,5,25])}")