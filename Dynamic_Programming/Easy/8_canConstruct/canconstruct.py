# Note : do not take out any string from the middle as this will create new adjacent string that is not present in the original string
#        1) Always check the matching prefixes to avoid the above situation

# Default method :
def canConstruct_Default(target : str, wordBank : list[str]):
    print(target)
    # Base case : When the target is reduced down to an empty string, then the target string can be combined using the word from the wordBank
    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word) == True:
            temp = str(target)
            temp = temp.replace(word,"")
            if canConstruct(temp,wordBank) == True:
                return True

    return False

# Top-down approach [Memoisation]
def canConstruct(target : str, wordBank : list[str], memo = None):
    if memo == None:
        memo = {}

    if target in memo:
        return memo[target]

     # Base case : When the target is reduced down to an empty string, then the target string can be combined using the word from the wordBank
    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word) == True:
            temp = str(target)
            temp = temp.replace(word,"")
            if canConstruct(temp,wordBank) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False

# Tabulation : Create an array of size target+1 where the index=0 -> the empty string (base case) and only from index=1 will it represent the starting position of the target string.
#              target = "abcdef", table.index = 0 --> empty string, table.index = 1 --> a, table.index = 2 --> b ......
def canConstruct_Tabulation(target : str, wordBank : list[str]):
    # Create a table of size target + 1
    table = [False]*(len(target)+1)
    # Seed value --> Base Case : Empty String is always True
    table[0] = True

    for index in range(len(target)+1):
        if table[index] == True:
            for word in wordBank:
                if target.startswith(word,index,index+len(word) == True): # Check if the target string starting from index actually starts and ends with word.
                    index_forward = index + len(word)
                    if index_forward <= len(target):
                        table[index_forward] = True # if we can find a substring that starts and ends with the word, then set index+len(word) to be true.

    return table[len(target)]

# m = target.length
# n = wordBank.length

# BruteForce
# O(n^m*m) ->(worst case) where the height of the tree is m, the branching factor is n and the additional processing with copying and slicing the target string.
# O(m*m) -> height of the tree which is the call stack plus maintaining the new sliced string at every call stack

# Memoisation
# O(n*m*m)
# O(m)

if __name__=="__main__":
    target = "abcdef"
    wordBank = ["ab","abc","cd","def","abcd"]
    print(f"(Memoisation) Can the target word : {target} be combined from the words in the wordBank ? {canConstruct(target,wordBank)}")
    print(f"(Tabulation) Can the target word : {target} be combined from the words in the wordBank ? {canConstruct_Tabulation(target,wordBank)}")
    print(f"(Default) Can the target word : skateboard be combined from the words in the wordBank ? {canConstruct_Default('skateboard',['bo','rd','ate','t','ska','sk','boar']) }")
    print(f"(Tabulation) Can the target word : skateboard be combined from the words in the wordBank ? {canConstruct_Tabulation('skateboard',['bo','rd','ate','t','ska','sk','boar']) }")
    print(f"(Memoisation) Can the target word : eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef be combined from the words in the wordBank ? {canConstruct_Default('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']) }")
    print(f"(Tabulation) Can the target word : eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef be combined from the words in the wordBank ? {canConstruct_Tabulation('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']) }")
