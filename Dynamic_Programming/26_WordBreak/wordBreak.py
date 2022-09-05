# Method 1 : Naive Recursion
def wordBreak(s: str, wordDict: list[str]) -> bool:
    # Base case - empty string always return true because there is no list required to create it.
    if s == "":
        return True

    # Note : Always checks for equivalent prefix so as to avoid creating unseen substring that is not in the wordDict. This can be done using str.startswith(string).
    for word in wordDict:
        if s.startswith(word) == True:
            temp = s
            temp = temp.replace(word,"")
            if wordBreak(temp,wordDict) == True:
                return True

    return False

# Method 2 : Memoisation
def wordBreak_Memoisation(s: str, wordDict: list[str], memo=None) -> bool:
    # dictionary that stores all subproblems result.
    print(memo)
    if memo == None:
        memo = {}
    
    # Search for the repeated subproblems result in the dictionary.
    if s in memo:
        return memo[s]

    # Base case - empty string always return true because there is no list required to create it.
    if s == "":
        return True

    # Note : Always checks for equivalent prefix so as to avoid creating unseen substring that is not in the wordDict. This can be done using str.startswith(string).
    for word in wordDict:
        if s.startswith(word) == True:
            temp = s
            temp = temp.replace(word,"")
            if wordBreak(temp,wordDict) == True:
                memo[s] = True
                return memo[s]

    memo[s] = False
    return memo[s]

# Method 3 : Tabulation - Top down approach (starting from index 0)
def wordBreak_Tabulation_TD(s: str, wordDict: list[str]) -> bool:
    # Create a table of size s + 1 because we're gonna be using the extra index at position 0 to serve as the starting point for the algo.
    # Note : Only starting from index 1 will it represent the initial string character of 0, from index 2 represents string character of 1 .... so on.
    table = [False] * (len(s)+1) 
    # Seed value - an empty string will always be True for any wordDict.
    table[0] = True

    for i in range(len(s)):
        if table[i] == True: # Only proceed if the starting character of the string s is equal to the word in wordDict.
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: # Check if the character so far at i 
                    table[i+len(word)] = table[i] 
                
    return table[len(s)]

# Method 3 : Tabulation - Bottom Up approach (starting from index len(s) - the end)
def wordBreak_Tabulation_BU(s: str, wordDict: list[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: 
                    dp[i] = dp[i+len(word)]
                if dp[i] == True:
                    break
     
    return dp[0]
        
if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(f"Can {s} can be segmented by {wordDict} ? {wordBreak(s,wordDict)}")
    print(f"Can {s} can be segmented by {wordDict} ? {wordBreak_Memoisation(s,wordDict)}")
    print(f"Can {s} can be segmented by {wordDict} ? {wordBreak_Tabulation_TD(s,wordDict)}")
    print(f"Can {s} can be segmented by {wordDict} ? {wordBreak_Tabulation_BU(s,wordDict)}")
    print(f'Can {"catsandog"} can be segmented by {["cats","dog","sand","and","cat"]} ? {wordBreak_Tabulation_TD(s,["cats","dog","sand","and","cat"])}')
    print(f'Can {"catsandog"} can be segmented by {["cats","dog","sand","and","cat"]} ? {wordBreak_Tabulation_BU(s,["cats","dog","sand","and","cat"])}')

