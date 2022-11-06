# Method 1 : Naive Recursion
def lengthOfLIS(nums: list[int]) -> int:
    return LIS_Helper(0,-1,nums,len(nums))

def LIS_Helper(curr_index, prev_index, nums : list[int], size):
    # Base case
    if curr_index == size: # It might be weird to count an extra index after the end of the list but it is necessary in order to correctly return the number of LIS.
        return 0

    not_taken = LIS_Helper(curr_index+1,prev_index,nums,size) # Case 1 : Not selecting the current element at current_index
    taken = 0
    if prev_index == -1 or nums[curr_index] > nums[prev_index]:
        taken = 1 + LIS_Helper(curr_index+1,curr_index,nums,size) # Case 2 : Selecting the current element at current_index

    return max(taken, not_taken) # check which branch of decision will give the maximum LIS.

# Method 2 : Memoisation
def lengthOfLIS_Memoisation(nums: list[int]) -> int:
    return LIS_Helper_Memoisation(0,-1,nums,len(nums))

def LIS_Helper_Memoisation(curr_index, prev_index, nums : list[int], size, memo = None):
    # Dictionary for all the repeated subtrees solution : f(curr_index, prev_index) f(0,-1) -> f(1,-1) -> f(2,-1) -> f(3,-1) -> ......
    if memo == None:
        memo = {}
    # Create a key for storing and identifying the repeated subtrees solution.
    key = str(curr_index) + ' ' + str(prev_index)
    if key in memo:
        return memo[key]

    # Base case
    if curr_index == size:
        return 0

    not_taken = LIS_Helper_Memoisation(curr_index+1, prev_index, nums, size, memo)
    taken = 0
    if prev_index == -1 or nums[curr_index] > nums[prev_index]:
        taken = 1 + LIS_Helper_Memoisation(curr_index+1, curr_index, nums, size, memo)

    memo[key] = max(not_taken, taken) # Stores the instance of every LIS
    return memo[key]

# Method 3 : DP - Tabulation
def lengthOfLIS_Tabulation(nums: list[int]) -> int:
    # Table of size of nums, By default all elements is of length 1 by itself.
    table = [1] * (len(nums))

    # Use the concept of subproblems to solve:
    #     f(5) -> LIS = 1
    #     /  \
    # f(5)    empty

    #             f(4) -> LIS = 1 + max(f(5))
    #             /  \
    #         f(5)    f(5)
    #         /  \    /  \
                
    #             f(3) -> LIS = 1 + max(f(4) or f(5))
    #             /  \
    #         f(4)    f(4)
    #         /  \    /  \
    #     f(5)   f(5)f(5) f(5)
    for i in reversed(range(len(nums))):
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                table[i] = max(table[i], 1 + table[j])
    
    return max(table)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(f"Naive Recursion")
    print(f"The longest increasing subsequence for {nums} is {lengthOfLIS(nums)}")
    print(f"The longest increasing subsequence for {[0,1,0,3,2,3]} is {lengthOfLIS([0,1,0,3,2,3])}")
    print(f"The longest increasing subsequence for {[7,7,7,7,7,7,7]} is {lengthOfLIS([7,7,7,7,7,7,7])}")

    print(f"Memoisation")
    print(f"The longest increasing subsequence for {nums} is {lengthOfLIS_Memoisation(nums)}")
    print(f"The longest increasing subsequence for {[0,1,0,3,2,3]} is {lengthOfLIS_Memoisation([0,1,0,3,2,3])}")
    print(f"The longest increasing subsequence for {[7,7,7,7,7,7,7]} is {lengthOfLIS_Memoisation([7,7,7,7,7,7,7])}")

    print("Tabulation")
    print(f"The longest increasing subsequence for {nums} is {lengthOfLIS_Tabulation(nums)}")
    print(f"The longest increasing subsequence for {[0,1,0,3,2,3]} is {lengthOfLIS_Tabulation([0,1,0,3,2,3])}")
    print(f"The longest increasing subsequence for {[7,7,7,7,7,7,7]} is {lengthOfLIS_Tabulation([7,7,7,7,7,7,7])}")
