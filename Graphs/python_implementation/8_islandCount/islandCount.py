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
  ['W', 'W'],
  ['W', 'W'],
]

# Given a 2D grid where each cell is assign either as a Land ("l") or Water ("W"), find all the individual graph components indicated by the "L".
# Brief description of how the algo works :
#     Loop through each of the cell, skips the cell with "W" or the cell with "L" but is marked as visited, explore the cell with "L" using DFS, once finished exploring, increment the count by 1.

# My implementation
def DFS(grid, s_r, s_c, visited):
    # Vector that represent the up, down, left and right movement of the node in the grid
    rowVector = [-1,1,0,0]
    colVector = [0,0,-1,1]

    # The typical DFS algo
    queue = [f"{s_r} {s_c}"] 
    
    while len(queue) != 0:
        currNode = queue.pop()
        curr_r, curr_c = currNode.split()

        # The are only 4 possible neighbours for each node which are in the top, down, left and right directions.
        for index in range(4):
            newRow = int(curr_r) + rowVector[index]
            newCol = int(curr_c) + colVector[index]

            # Making sure that we skip any new indexes that are out of bound
            if newRow < 0 or newRow > len(grid)-1:
                continue
            if newCol < 0 or newCol > len(grid[0])-1:
                continue
            # Skip the grid that is not land.
            if grid[newRow][newCol] == "W":
                continue
            # Skip the grid that has been visited.
            if f"{newRow} {newCol}" in visited:
                continue
            
            visited.add(f"{newRow} {newCol}")
            queue.insert(0,f"{newRow} {newCol}")

# Alvin Zablan's implementation
def DFS_Recur(grid, r, c, visited):
    # Check if the new row and col are not out of bound
    # Both rows and cols must be between 0 and the respective grid axis length
    rowInbounds = (0 <= r) and (r < len(grid))
    colInbounds = (0 <= c) and (c < len(grid[0]))
    if not rowInbounds or not colInbounds:
        return False

    # If the new grid pos is 'W':
    if grid[r][c] == 'W':
        return False

    # If the new grid pos has already been visited :
    pos = f"{r} {c}"
    if pos in visited:
        return False

    visited.add(pos)

    # DFS recursion for each neighbouring direction (top, down, left, right)
    DFS_Recur(grid, r-1, c, visited)
    DFS_Recur(grid, r+1, c, visited)
    DFS_Recur(grid, r, c-1, visited)
    DFS_Recur(grid, r, c+1, visited)

    # If successfully explore a given island without triggering any of the previous conditions
    return True


def islandCount(grid):
    visited = set()
    count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            # Alvin Zablan's implementation
            if (DFS_Recur(grid, row, col, visited) == True):
                count += 1

            # My implementation
            # # Skip cells that are not Land
            # if grid[row][col] == 'W':
            #     continue
            # # Skip cells that have been visited
            # if f"{row} {col}" in visited:
            #     continue
            # # Run the DFS to populate the visited set
            # DFS(grid, row, col, visited)

            # # If DFS succeeds, increment count by 1
            # count += 1

    return count

# Time : 
#      r = # rows
#      c = # cols
#      O(r*c) - worst case : the whole grid is a single graph component
# Space :
#      O(r*c)
if __name__ == "__main__":
    print(f"The number of islands in grid1 is {islandCount(grid)}")
    print(f"The number of islands in grid2 is {islandCount(grid2)}")
    print(f"The number of islands in grid3 is {islandCount(grid3)}")
    print(f"The number of islands in grid4 is {islandCount(grid4)}")
