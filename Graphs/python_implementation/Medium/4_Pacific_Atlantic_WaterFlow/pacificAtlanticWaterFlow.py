def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    row, col = len(heights), len(heights[0])
    def DFS_Recur(r, c, visit, prevHeights):
        # Check out of bounds
        rowInbounds = (0 <= r) and (r < row)
        colInbounds = (0 <= c) and (c < col)

        if not rowInbounds or not colInbounds:
            return

        # Check if already in visited set
        if (r,c) in visit:
            return

        # Main algo : Check if the current position heights is lager than previous position heights - (we're moving in the opposite direction(ascending order) which is from ocean to the cells that can flow to both pacific and atlantic)
        if heights[r][c] < prevHeights:
            return

        visit.add((r,c))

        # Note : the prevHeights should be the current iter r and c as in the next iter, the r and c will have changed.
        DFS_Recur(r-1,c,visit,heights[r][c])
        DFS_Recur(r+1,c,visit,heights[r][c])
        DFS_Recur(r,c-1,visit,heights[r][c])
        DFS_Recur(r,c+1,visit,heights[r][c])

        return

    atlantic, pacific = set(), set()
    # Explore all the nodes in the top(pacific) and bottom(atlantic) of the grid
    for c in range(col):
        # Explore the top end of pacific nodes - Note : let the first instance of the algo to have the same prevHeights as itself, to allow the algo to run.
        DFS_Recur(0,c,pacific,heights[0][c])
        # Explore the bottom end of atlantic nodes
        DFS_Recur(row-1,c,atlantic,heights[row-1][c])

    # Explore all the nodes in the right(atlantic) and left(pacific) of the grid
    for r in range(row):
        # Explore the right end of atlantic nodes
        DFS_Recur(r,0,pacific,heights[r][0])
        # Explore the left end of pacific nodes
        DFS_Recur(r,col-1,atlantic,heights[r][col-1])

    result = []
    # Add the position into the result - if and only if that position (visited node) exist in both the atlantic and pacific sets
    for r in range(row):
        for c in range(col):
            if (r,c) in atlantic and (r,c) in pacific:
                result.append([r,c])
 
    return result

if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(f"The cells that can flow to both the Atlantic and Pacific are {pacificAtlantic(heights)}")