# Default Method:
def canSum_Default(targetSum, numbers : list[int]):
    # base case
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        diff = targetSum - num
        # The idea here is that when the sum is possible, we immediately return true to terminate the entire function.
        if canSum(diff, numbers) == True:
            return True

    return False

# Method 1 : Top-down approach using memoisation
def canSum(targetSum, numbers : list[int], memo = None):
    # print(memo)
    # To prevent dictionary from being mutated every call due to the default argument memo = {}.
    if memo == None:
        memo = {}

    # cache the repeated subtrees results
    if targetSum in memo:
        return memo[targetSum]

    # base case
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        diff = targetSum - num
        # The idea here is that when the sum is possible, we immediately return true to terminate the entire function.
        if canSum(diff, numbers, memo) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

# Method 2 : Still insisting on using the default memo={}, here we use a dummy variable targetDict to point to the key value pairs in the memo (targetDict = memo[targetsum]),
#            then storing the {numbers : true/false} in it for future use.
def canSum_1(targetSum, numbers, memo={}):
    numbersTuple = tuple(numbers)
    # print(memo)
    if targetSum in memo:
        targetDict = memo[targetSum]
        if numbersTuple in targetDict:
            return targetDict[numbersTuple]
    else:
        memo[targetSum] = {}

    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for n in numbers:
        remainder = targetSum - n
        if canSum_1(remainder, numbers, memo):
            targetDict = memo[targetSum]
            targetDict[numbersTuple] = True
            return True

    targetDict = memo[targetSum]
    targetDict[numbersTuple] = False
    return False

# Method Tabulation :
def canSum_Tabulation(targetSum : int, numbers : list[int]):
    # Initialise a list of size targetSum+1 -> the targetSum is changing as it is deducted down to 0 by the numbers in the previous methods.
    table = [False] * (targetSum+1)
    # Seed value -> A targetSum=0 is always possible with an empty []
    table[0] = True

    # Take each index of table(0,1,2,3,4,....,targetSum) and add each of the corresponding numbers to it, then set those incremented positions as True.
    # The index represents all the possible sums that can be obtained via the given numbers.
    for pos in range(targetSum):
        if table[pos] == True: # Only when it is true that we can look ahead.
            for num in numbers:
                index_forward = pos + num
                if index_forward <= targetSum:
                    table[index_forward] = table[pos]
                    
        
    return table[targetSum]

if __name__ == "__main__":
    targetSum = 7
    numbers = [5,3,4,7]
    print(f"(Memoisation) Can the elements in the array numbers = {numbers} sum up to {targetSum} ? {canSum(targetSum, numbers)}")
    print(f"(Tabulation) Can the elements in the array numbers = {numbers} sum up to {targetSum} ? {canSum_Tabulation(targetSum, numbers)}")
    print(f"(Memoisation) Can the elements in the array numbers = {[7,14]} sum up to {3000} ? {canSum(3000, [7,14])}")
    print(f"(Tabulation) Can the elements in the array numbers = {[7,14]} sum up to {3000} ? {canSum_Tabulation(3000, [7,14])}")

