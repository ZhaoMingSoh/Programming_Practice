# Naive Method - Recursion
def combinationSum3(k: int, n: int) -> list[list[int]]:
    candidates = [i for i in range(1,10)]
    res = []
    def combSum3_Helper(pos,k,n,candidates,res,sum_comb):
        # Base Case
        if n == 0:
            # Get the combination list of only len(k)
            if len(sum_comb) == k:
                res.append(list(sum_comb))
            return
        if n < 0:
            return
        
        # Idea : We can only choose each index once at each level of the tree but indexes greater than it can be chosen using a loop.
        for i in range(pos,len(candidates)): # We can only use each index at most once.
            sum_comb.append(candidates[i])
            combSum3_Helper(i+1,k,n-candidates[i],candidates,res,sum_comb) # Call onto the next index val
            sum_comb.pop() # Remove children's elements from the combination list

    combSum3_Helper(0,k,n,candidates,res,[])
    return res

if __name__ == "__main__":
    k = 3
    n = 7
    print(f"The list of possible combinations of size {k} from numbers between 1 to 9 for {n} is {combinationSum3(k,n)}")