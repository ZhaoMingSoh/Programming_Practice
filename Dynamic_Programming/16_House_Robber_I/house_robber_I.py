# Naive Recursion:
def rob(nums: list[int]) -> int:
    def rob_Helper(pos, nums):
        # Base Case
        if pos == len(nums)-1:
            return nums[pos]
        if pos > len(nums)-1: # Out of bounds simply return 0
            return 0
        
        taken = nums[pos] + rob_Helper(pos+2,nums) # If current pos is chosen then it has to choose the next pos+2
        not_taken = rob_Helper(pos+1,nums) # If current pos is not chosen then it can choose the next pos+1

        return max(taken,not_taken) # find the max of the two

    return rob_Helper(0,nums)

# Memoisation:
def rob_Memo(nums: list[int]) -> int:
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
        
        taken = nums[pos] + rob_Helper_Memo(pos+2,nums, memo) # If current pos is chosen then it has to choose the next pos+2
        not_taken = rob_Helper_Memo(pos+1,nums, memo) # If current pos is not chosen then it can choose the next pos+1

        memo[pos] = max(taken,not_taken)
        return memo[pos] # find the max of the two

    return rob_Helper_Memo(0,nums)

# Tabulation:
def rob_Tabulation(nums: list[int]) -> int:
    # Create a table of size nums + 1
    table = [0] * (len(nums)+1)

    # Idea : Gradually build up the solution to each of the table indexes from the previous indexes.
    #       - Always start at table[1] because table[0] represents robbing no houses.
    #       - take = nums[i-1] + table[i-2], not take = table[i-1]
    #       - Ex: houses = [1 2 3 1] - table = [0 0 0 0 0]
    #                       0 1 2 3             0 1 2 3 4
    #             1)(subproblems for i=1 is either go 2 steps before or 1 step before) table[1] = max(nums[0]+table[-1], table[0]) -> 1   table = [0 1 0 0 0]
    #                                                                                                                                              0 1 2 3 4
    for i in range(1,len(nums)+1): # Starts from index=1 because index=0 refers to not robbing anything.
        taken = nums[i-1]
        if i-2 >= 0: # The first i=1 will lead to f(1-2=-1) which does not exist.
            taken += table[i-2]
        not_taken = table[i-1]
        table[i] = max(taken,not_taken)
        
    return table[len(nums)]

if __name__ == "__main__":
    nums = [1,2,3,1]
    print("Brute Force Recursion")
    print(f"The maximum amount of money you can rob is {rob(nums)}")

    print("\nMemoisation")
    print(f"The maximum amount of money you can rob is {rob_Memo(nums)}")

    print("\nTabulation")
    print(f"The maximum amount of money you can rob is {rob_Tabulation(nums)}")
