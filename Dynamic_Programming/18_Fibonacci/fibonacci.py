# Default Way :
def fib_default(n):
    if n == 1:
        return 1
    if n < 1:
        return 0

    return fib_default(n-1) + fib_default(n-2)

# (Top-down approach) : memoisation
def fib(n, memo = {}):
    print(f"n = {n}, memo = {memo}")
    # Returns the repeated subtree fibonacci value
    if memo.get(n):
        return memo[n]
    
    # base case
    if n == 1:
        return 1
    if n < 1:
        return 0
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    
    return memo[n]

# Tabulation technique : Fully iterative, we just need to iterate through the array to get the result
def fib_tabulation(n : int) :
    # Initialise an empty table with 0s
    table = [0]*(n+1)
    # Set value at index 1 to be 1
    if len(table) <= 1:
        return 0
    table[1] = 1
    print(table)
    # Iterate through the index of the table,
    # if n = 5, table = [0,1,0,0,0,0] -> add table[0] to i = 1 and i = 2
    #           table = [0,1,0,0,0,0] -> add table[1] to i = 2 and i = 3
    #           table = [0,1,1,1,0,0] -> add table[2] to i = 3 and i = 4
    #           table = [0,1,1,2,1,0] -> add table[3] to i = 4 and i = 5
    #           table = [0,1,1,2,3,2] -> add table[4] to i = 5
    #           table = [0,1,1,1,3,5]
    for i in range(len(table)):
        print(table)
        if i+1 <= len(table)-1:
            table[i+1] += table[i]
        if i+2 <= len(table)-1:
            table[i+2] += table[i]

    return table[n]

if __name__ == "__main__":
    # fib starts from 0 1 1 2 3 5 8 ....
    #                 0 1 2 3 4 5 6
    n = 6
    result = fib(n)
    print(f"(Memoisation)Fib for index {n} is {result}")
    print(f"(Tabulation)Fib for index {n} is {fib_tabulation(n)}")

