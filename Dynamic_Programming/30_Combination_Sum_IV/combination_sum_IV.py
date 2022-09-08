def combinationSum4(nums: list[int], target: int) -> int:
    # Base case
    if target == 0:
        return 1
    if target < 0:
        return 0
    
    val = 0
    # Idea : Brute force all nums at each level of the tree and increment the val by 1 for each instance of target reaching 0.
    for num in nums:
        diff = target - num
        val += combinationSum4(nums,diff) # only during returning time of the function call will the value be returned to be incremented at the parent's function call.

    return val

# Memoisation
def combinationSum4_Memo(nums: list[int], target: int) -> int:
    def combSum4_Helper_Memo(nums,target,memo=None):
        if memo == None:
            memo = {}
        
        if target in memo:
            return memo[target]

        # Base case
        if target == 0:
            return 1
        if target < 0:
            return 0
        
        val = 0
        for num in nums:
            diff = target - num
            val += combSum4_Helper_Memo(nums,diff,memo)

        memo[target] = val
        return memo[target]
    
    return combSum4_Helper_Memo(nums,target)

# DP - Tabulation
def combinationSum4_Tab(nums: list[int], target: int) -> int:
    # Create a table of size target + 1
    table = [0] * (target+1)
    # Seed Value
    table[0] = 1

    for i in range(1,target+1):
        for num in nums:
            if i-num < 0:
                continue
            table[i] += table[i-num]

    return table[target]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print("Default Recursion")
    print(f"The total number of possible combinations for {target} from {nums} is {combinationSum4(nums,target)}")
    print(f"The total number of possible combinations for {3} from {[9]} is {combinationSum4([9],3)}")

    print("\nMemoisation")
    print(f"The total number of possible combinations for {target} from {nums} is {combinationSum4_Memo(nums,target)}")
    print(f"The total number of possible combinations for {3} from {[9]} is {combinationSum4_Memo([9],3)}")

    print("\Tabulation")
    # nums = [1,2,3] target = 4 --> table of size 5 [1,0,0,0,0] --> start from position 1 and find the subproblem.
    #         0 1 2                                  0 1 2 3 4
    # DP[1] = DP[1-num[0]] + DP[1-num[1]] + DP[1-num[2]] : DP[1] = 1 + None(Out of bound) + None(Out of bound) = 1
    # DP[2] = DP[2-num[0]] + DP[2-num[1]] + DP[2-num[2]] : DP[2] = 1 + 1 + None = 2
    # DP[3] = DP[3-num[0]] + DP[3-num[1]] + DP[3-num[2]] : DP[3] = 2 + 1 + 1 = 4
    # DP[4] = DP[4-num[0]] + DP[4-num[1]] + DP[4-num[2]] : DP[4] = 4 + 2 + 1 = 7
    print(f"The total number of possible combinations for {target} from {nums} is {combinationSum4_Tab(nums,target)}")
    print(f"The total number of possible combinations for {3} from {[9]} is {combinationSum4_Tab([9],3)}")