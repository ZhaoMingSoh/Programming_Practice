def DFS_Recur(grid, r, c, visited):
    total_Perimeter = 0
    # Check if r,c are within the bound of the grid
    rowInbounds = (r >= 0) and (r < len(grid))
    colInbounds = (c >= 0) and (c < len(grid[0]))
    print(f"({r},{c}), {rowInbounds}, {colInbounds}, {visited}")
    # Water and Out of bounds (r,c) count towards the perimeter
    # If r or c are out of bound
    if not rowInbounds or not colInbounds:
        return 1

    # If current r,c is water
    if grid[r][c] == 0:
        return 1
    
    # Its a land that has already been visited, we do not want it to affect our total perimeter
    if f"{r},{c}" in visited:
        return 0

    visited.add(f"{r},{c}")

    total_Perimeter += DFS_Recur(grid, r+1, c, visited)
    total_Perimeter += DFS_Recur(grid, r-1, c, visited)
    total_Perimeter += DFS_Recur(grid, r, c+1, visited)
    total_Perimeter += DFS_Recur(grid, r, c-1, visited)

    # finished exploring a land, return its total perimeter so far
    return total_Perimeter

def IterativeApproach(grid):
    rows = len(grid) # say it is 4
    cols = len(grid[0]) # say it is 4

    result = 0

    for r in range(rows):
        for c in range(cols):
            # Only work for land
            if grid[r][c] == 1:
                # if r = 0 and we move up, r-1 = -1 (out of bounds); We set up=0
                if r == 0:
                    up = 0
                else:
                    # if r > 0, we can move up 
                    up = grid[r-1][c]
                
                # if c = 0 and we move left, c-1 = -1 (out of bounds); We set left=0
                if c == 0:
                    left = 0
                else:
                    # if c > 0, we can move left
                    left = grid[r][c-1]

                # if r = rows-1 -> 4-1 = 3 and we move down, r+1 = 4 (out of bounds); We set down=0
                if r == rows-1:
                    down = 0
                else:
                    # if r < rows-1, we can move down
                    down = grid[r+1][c]

                # if c = cols-1 -> 4-1 = 3 and we move right, r+1 = 4 (out of bounds); We set right=0
                if c == cols-1:
                    right = 0
                else:
                    # if c < cols-1, we can move right
                    right = grid[r][c+1]
                
                # A square has 4 sides of length 1, when we encounter a side that is land, we deduct it off from the length of 4
                result += 4-(up+left+right+down)
        
    return result
   

def islandPerimeter(grid: list[list[int]]) -> int:
    visited = set()
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                result += DFS_Recur(grid, r, c, visited)

    return result

if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    grid2 = [[1]]
    grid3 = [[1,0]]

    print(f"The total island perimeter for grid 1 is {islandPerimeter(grid)}")