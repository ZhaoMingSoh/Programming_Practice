# Method 1 : Brute force recursion is too slow as the complexity is O(2^n), DFS
def climbStairs(s : int,n : int):
    if s == n:
        return 1
    if s > n:
        return 0
    return climbStairs(s+1, n) + climbStairs(s+2, n)

# Method 2 : Memoisation (Top-down approach)
n = 3
memo = [0] * (n+1)
def climbStairs_Memo(n : int):
    # memoisation array
    if memo[n]:
        return memo[n]
    
    # base case
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    memo[n] = climbStairs_Memo(n-1) + climbStairs_Memo(n-2)
    
    return memo[n]

# Method 3 : Memoisation (Bottom-up approach) -> use array to store the solution to the n-1 and n-2 subproblems and use it to find n = n-1 + n-2.
#                                                [Using the base case where n=0 --> 1 step and n=1 --> 1 step.]
def climbStairs_Memo_BA(n : int):
    m = [0]*(n+1)
    m[0] = 1
    for i in range(1,n+1):
        if i == 1:
            m[i] = 1
            continue
        m[i] = m[i-1] + m[i-2]
  
    return m[n]

if __name__=="__main__":
    print(f"Number of 1 steps and 2 steps to reach {n} steps is {climbStairs_Memo_BA(n)}")