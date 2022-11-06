# Naive Recursion :
def rob(nums: list[int]) -> int:
    # Edge cases:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0],nums[1])
        
    def rob_Helper(pos, nums):
        # Base Case
        if pos == len(nums)-1:
            return nums[pos]
        if pos > len(nums)-1: # Out of bounds simply return 0
            return 0
        
        taken = nums[pos] + rob_Helper(pos+2,nums) # If current pos is chosen then it has to choose the next pos+2
        not_taken = rob_Helper(pos+1,nums) # If current pos is not chosen then it can choose the next pos+1

        return max(taken,not_taken) # find the max of the two

    return max(rob_Helper(0,nums[1:]),rob_Helper(0,nums[:len(nums)-1]))

# Memoisation :
def rob_Memo(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0],nums[1])

    def rob_Helper_Memo(pos, nums, memo=None):
        if memo == None:
            memo = {}
        
        if pos in memo:
            return memo[pos]

        # Base Case
        if pos == len(nums)-1:
            return nums[pos]
        if pos > len(nums)-1: # Out of bounds simply return 0
            return 0
        
        taken = nums[pos] + rob_Helper_Memo(pos+2,nums) # If current pos is chosen then it has to choose the next pos+2
        not_taken = rob_Helper_Memo(pos+1,nums) # If current pos is not chosen then it can choose the next pos+1

        memo[pos] = max(taken, not_taken)
        return memo[pos] # find the max of the two

    return max(rob_Helper_Memo(0,nums[1:]),rob_Helper_Memo(0,nums[:len(nums)-1])) # the only change we made to the house robber 1 solution is we run the algo for 2 separate instances where the first uses a nums without the first element and the second uses a nums without the last element.
                                                                                  # Explanation : this is because the houses are connected in a circle meaning the first and last houses can never be selected as they are adjacent to each other.

# Tabulation :
def rob_Tab(nums : list[int]):
    # Edge cases:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0],nums[1])

    def rob_helper_Tab(nums):
        # Table of size len(nums) + 1
        table = [0] * (len(nums)+1)
    
        for pos in range(1,len(nums)+1):
            take = nums[pos-1]
            if pos-2 >= 0:
                take += table[pos-2]
            not_take = table[pos-1]
            table[pos] = max(take,not_take)

        return table[len(nums)]
    
    return max(rob_helper_Tab(nums[1:]),rob_helper_Tab(nums[:len(nums)-1]))

if __name__ == "__main__":
    nums = [1,2,3,1]
    print("\nNaive Recursion")
    print(f"The maximum amount of money you can rob without alerting police is {rob(nums)}")

    print("\nMemoisation")
    print(f"The maximum amount of money you can rob without alerting police is {rob_Memo(nums)}")
    
    print("\nTabulation")
    print(f"The maximum amount of money you can rob without alerting police is {rob_Tab(nums)}")


