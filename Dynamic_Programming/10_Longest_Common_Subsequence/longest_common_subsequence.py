# Method 1 : Default Naive Recursion
def longestCommonSubsequence(text1: str, text2: str) -> int:
    return LCS_Helper(0,0,text1, text2)

def LCS_Helper(i, j, text1, text2):
    # Base case
    if i == len(text1) or j == len(text2):
        return 0
    
    # Case 1 : The text at current index i and j are the same, then add 1 and call itself with i+1 and j+1
    if text1[i] == text2[j]:
        return 1 + LCS_Helper(i+1,j+1,text1,text2)
    
    # Case 2 : The text at the current index i and j are not the same, then go on each side to check (this will ensure that the order remains)
    return max(LCS_Helper(i+1,j,text1,text2),LCS_Helper(i,j+1,text1,text2))

# Method 2 : Memoisation
def longestCommonSubsequence_Memoisation(text1 : str, text2 : str):
    return LCS_Helper_Memoisation(0,0,text1,text2)

def LCS_Helper_Memoisation(i,j,text1,text2,memo=None):
    if memo == None:
        memo = {}

    # Create the key for that represent each instance of the subtree
    # i=0 and j=0, key=0 0 || i=5 and j=3, key=5 3
    key = str(i) + ' ' + str(j)
    if key in memo:
        return memo[key]

    # Base case
    if i == len(text1) or j == len(text2):
        return 0

    # Case 1 : The text at current index i and j are the same, then add 1 and call itself with i+1 and j+1 (move both indexes)
    if text1[i] == text2[j]:
        return 1 + LCS_Helper_Memoisation(i+1,j+1,text1,text2,memo)

    # Case 2 : The text at the current index i and j are not the same, then go on each side to check (this will ensure that the order remains)
    # Starts with the left index representing text1, only after the result for the left index has been found, only then starts the right index representing text2
    memo[key] = max(LCS_Helper_Memoisation(i+1,j,text1,text2),LCS_Helper_Memoisation(i,j+1,text1,text2))
    return memo[key]

# Method 3 : Tabulation
# Time : O(n*m)
# Space : O(n*m)
def longestCommonSubsequence_Tabulation(text1 : str, text2 : str):
    # 2D table of size len(text1)+1 * len(text2)+1
    # Why do we have an extra row and col ? Why do we initialise everything to 0 val ?
        # The extra row and col is sort of the base case where when we have an empty string, then there does not exist any common subsequence, which is why they are all 0s.
        # The cells in the table represent the subproblems of the LCS.
    table = [[0 for r in range(len(text1)+1)] for c in range(len(text2)+1)]

    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if text2[i-1] == text1[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table[len(table)-1][len(table[0])-1]

if __name__ == "__main__":
    text1 = "ezupkr"
    text2 = "ubmrapg" 
    print(f"The longest common subsequence of the two texts {text1} and {text2} is {longestCommonSubsequence(text1,text2)}")
    print(f"The longest common subsequence of the two texts {text1} and {text2} is {longestCommonSubsequence_Memoisation(text1,text2)}")
    print(f"The longest common subsequence of the two texts {text1} and {text2} is {longestCommonSubsequence_Tabulation(text1,text2)}")
