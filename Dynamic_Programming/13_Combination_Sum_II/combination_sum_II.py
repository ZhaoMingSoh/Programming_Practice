# Naive Recursion - 
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    candidates.sort()
    def combSum2_Helper(i, candidates, target, sum_comb):
        # Base Case
        if target == 0:
            res.append(list(sum_comb))
            return
        if target < 0:
            return

        prev = -1 # prevents the use of duplicate candidates in the list of combination - 1) starts off with -1 which will not be present in the candidate list which will make sure that the first instance of the candidate can proceed without any issue.
        for k in range(i,len(candidates)): # to ensure the use of each index is at most once.
            if candidates[k] == prev: # check to see if the next candidate is a duplicate of the previously selected candidate at the level of the tree.
                continue
            sum_comb.append(candidates[k])
            combSum2_Helper(k+1, candidates, target-candidates[k], sum_comb)
            sum_comb.pop() # make sure that when a function call ends, the parent will revert its combination of candidates of its children by chopping them off.
            prev = candidates[k] # happens at the returning time of the function call, where the previous candidate will be recorded ensuring that no duplicate can be selected at the same tree level.

    combSum2_Helper(0, candidates, target, [])
    return res

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(f"The unique combination of {candidates} that sum to {target} is {combinationSum2(candidates,target)}")
    print(f"The unique combination of {[2,5,2,1,2]} that sum to {5} is {combinationSum2([2,5,2,1,2],5)}")
    print(f"The unique combination of {[2,1,2,1,1]} that sum to {4} is {combinationSum2([2,1,2,1,1],4)}")