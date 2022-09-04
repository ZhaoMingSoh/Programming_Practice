# Idea : When we move down or right in the 
# Default-way :
def gridtraveler_default(n,m):
    # base case
    if n == 0 or m == 0:
        return 0
    
    if n == 1 and m == 1:
        return 1

    return gridtraveler(n-1, m) + gridtraveler(n, m-1)

# Top-down approach using memoisation
def gridtraveler(n : int, m : int, memo = {}):
    key = str(f"{n},{m}")
    
    # Check if the repeated subtrees results are in the memo dict
    if memo.get(key):
        return memo[key]
    
    # base case
    if n == 0 or m == 0:
        return 0
    
    if n == 1 and m == 1:
        return 1
    
    # going down -> n-1 and going right -> m-1
    memo[key] = gridtraveler(n-1, m, memo) + gridtraveler(n, m-1, memo)
    
    return memo[key]

# Tabulation technique : 
def gridTraveler_tabulation(n : int, m : int):
    table = [[0 for r in range(m+1)] for c in range(n+1)] # create a 2d list of size n+1 by m+1

    if n == 0 or m == 0:
        return 0

    table[1][1] = 1 # set the position at n=1 and m=1 to 1

    print(len(table), len(table[0]))
    for r in range(len(table)):
        for c in range(len(table[0])):
            if c+1 <= len(table[0])-1:
                table[r][c+1] += table[r][c] # go right
            if r+1 <= len(table)-1:
                table[r+1][c] += table[r][c] # go down

    return table[n][m]

if __name__ == "__main__":
    n = 2 # row
    m = 3 # col
    print(f"(Memoisation) Number of ways to traverse grid[{n},{m}] using only right and down motions is {gridtraveler(n, m)}")
    print(f"(Tabulation) Number of ways to traverse grid[{n},{m}] using only right and down motions is {gridTraveler_tabulation(n, m)}")
