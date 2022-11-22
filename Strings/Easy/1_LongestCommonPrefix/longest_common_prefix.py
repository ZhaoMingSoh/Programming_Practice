import math

# Horizontal Scanning :
def longestCommonPrefix_HS(strs : str) -> str:
    res = ""

    # Compare the first char of the first string with the first char of all other strings and so on ....
    for i in range(len(strs[0])):
        for s in strs:
            # If it so happens that one of the other strings is smaller in length than the first string.
            # If the char at index i of the first string is not the same as one of the other strings.
            if i == len(s) or s[i] != strs[0][i]:
                return res
        # The char at index i of string one certainly exist at index i of all other strings.
        res += strs[0][i]

    return res

# Horizontal Scanning 2 : compare 2 strings at a time and find their common prefix, once the common prefix is found, take it and compare to the string 1 index from the current index. 
#                         The way we get the common prefix is by shrinking the existing prefix of the first string until it becomes the common prefix with whatever current string it is compared to.
def longestCommonPrefix_HS_2(strs : str) -> str:
    prefix = strs[0]
    for i in range(1,len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[0:len(prefix)-1]
    return prefix

# Divide and Conquer method :
#   n = strings in array, m = len of array
#   Time Complexity : 2*O(n/2) + O(m)
#   Space Complexity : O(m*log n) - log n recursive calls are stored on the execution stacks and each of the calls need m of space to store results
def longestCommonPrefix(strs : str) -> str:
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
    print(f"(Horizontal Scanning) The longest common prefix of {strs} is {longestCommonPrefix_HS(strs)}")
    print(f"(Horizontal Scanning) The longest common prefix of {strs} is {longestCommonPrefix_HS_2(strs)}")
    strs2 = ["dog","racecar","car"] # ""
    print(f"The longest common prefix of {strs2} is {longestCommonPrefix(strs2)}")
    print(f"(Horizontal Scanning) The longest common prefix of {strs2} is {longestCommonPrefix_HS(strs2)}")
    print(f"(Horizontal Scanning) The longest common prefix of {strs2} is {longestCommonPrefix_HS_2(strs2)}")
