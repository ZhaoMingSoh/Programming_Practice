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

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print("Default Recursion")
    print(f"The total number of possible combinations for {target} from {nums} is {combinationSum4(nums,target)}")
    print(f"The total number of possible combinations for {3} from {[9]} is {combinationSum4([9],3)}")

    print("\nMemoisation")
    print(f"The total number of possible combinations for {target} from {nums} is {combinationSum4_Memo(nums,target)}")
    print(f"The total number of possible combinations for {3} from {[9]} is {combinationSum4_Memo([9],3)}")