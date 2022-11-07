import math

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

grid2 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

grid3 = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

grid4 = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

def DFS_Recur(grid, r, c, visited):
    # Same as the implementation from question 8_islandCount
    rowInbounds = (0 <= r) and (r < len(grid))
    colInbounds = (0 <= c) and (c < len(grid[0]))
    if not rowInbounds or not colInbounds:
        return 0
    
    if grid[r][c] == 'W':
        return 0
    
    pos = f"{r} {c}"
    if pos in visited:
        return 0

    visited.add(pos)

    size = 1 # ensure that everytime we visit a valid node, it will return 1 to the previous call

    size += DFS_Recur(grid, r+1, c, visited)
    size += DFS_Recur(grid, r-1, c, visited)
    size += DFS_Recur(grid, r, c-1, visited)
    size += DFS_Recur(grid, r, c+1, visited)

    return size

def minimumIsland(grid):
    visited = set()
    islandSize = math.inf

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = DFS_Recur(grid, row, col, visited)
            if size > 0 and size < islandSize: # a size of 0 is an invalid size therefore we should omit it, choose the smallest size
                islandSize = size
    return islandSize

# Time Complexity : 
#   r = # rows
#   c = # cols
#   O(r*c)
# Space :
#   O(r*c)
if __name__ == "__main__":
    print(f"The minimum island size for graph1 is {minimumIsland(grid)}")
    print(f"The minimum island size for graph2 is {minimumIsland(grid2)}")
    print(f"The minimum island size for graph3 is {minimumIsland(grid3)}")
    print(f"The minimum island size for graph4 is {minimumIsland(grid4)}")