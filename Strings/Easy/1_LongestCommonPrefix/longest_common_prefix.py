import math

# Divide and Conquer method :
#   n = strings in array, m = len of array
#   Time Complexity : 2*O(n/2) + O(m)
#   Space Complexity : O(m*log n) - log n recursive calls are stored on the execution stacks and each of the calls need m of space to store results
def longestCommonPrefix(strs: list[str]) -> str:
    # 1. Divide the strs into l, mid, r, 
    # 2. then recursively split the divided l and r until the l index and r index are equal which then returns the strs[l] to the previous calls.
    # 3. when we get a single left string and a single right string from either end of the strs, we get the their longest common prefix, then return it to the previous calls.
    # 4. repeat (3) until the last 2 strings in the strs.
    def divideAndConquer(s, l, r):
        if l == r:
            return s[l]
        else:
            # The mid index has to be the floor of (l+r)/2 or else the left recursive call will never end.
            mid = math.floor((l+r) / 2)
            leftS = divideAndConquer(s, l, mid)
            rightS = divideAndConquer(s, mid+1, r)
            return commonPrefix(leftS,rightS)                

    def commonPrefix(leftS, rightS):
        smallestL = min(len(leftS),len(rightS))
        for i in range(smallestL):
            if leftS[i] != rightS[i]:
                return leftS[0:i]
        return leftS[0:smallestL]

    if strs == None or len(strs) == 0:
        return ""
    return divideAndConquer(strs,0,len(strs)-1)

if __name__ == "__main__":
    strs = ["flower","flow","flight"] # "fl"
    print(f"The longest common prefix of {strs} is {longestCommonPrefix(strs)}")
    strs2 = ["dog","racecar","car"] # ""
    print(f"The longest common prefix of {strs2} is {longestCommonPrefix(strs2)}")
