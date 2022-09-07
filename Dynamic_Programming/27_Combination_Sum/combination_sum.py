# Naive Method : Recursion - No memoisation possible because each subtree is distinct from the other subtrees in terms of what the combination.
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    list_sumcomb = [] # The main list that remembers all the unique combinations.
    combSum_Helper(candidates,0,target,list_sumcomb,None)
    return list_sumcomb

def combSum_Helper(candidates: list[int], i : int, target : int, list_sumcomb : list[list[int]], sum_comb):
    if sum_comb == None:
        sum_comb = []

    # Base case
    # Only when the target becomes zero do we know that we have found a possible unique combination
    if target == 0:
        list_sumcomb.append(list(sum_comb))
        return

    if i == len(candidates):
        return
    # ( Ensures that the combination is always unique - as we have 2 branches at each subtree where the left can choose 2 but the right can never choose 2.)
    # Case 1 : Keep choosing the same candidate index value until it no longer is <= target
    if candidates[i] <= target:
        sum_comb.append(candidates[i])
        combSum_Helper(candidates,i,target-candidates[i],list_sumcomb,sum_comb)
        sum_comb.pop() # Whenever the subtrees lead to no solution either by candidate[i] > remaining target value, 
                       # return to the previous subtrees, in doing so, we also have to remove whatever candidate value that was added to the sum_comb as the sum_comb is static.

    # Case 2 : Choose the next candidate index value when the previous does not work anymore.
    combSum_Helper(candidates,i+1,target,list_sumcomb,sum_comb)

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print("Naive Recursion: ")
    print(f"All unique combinations of {candidates} that sum to {target} is {combinationSum(candidates,target)}")
    print(f"All unique combinations of {[2,3,5]} that sum to {8} is {combinationSum([2,3,5],8)}")
    print(f"All unique combinations of {[2]} that sum to {1} is {combinationSum([2],1)}")
    print(f"All unique combinations of {[1,2]} that sum to {4} is {combinationSum([1,2],4)}")
