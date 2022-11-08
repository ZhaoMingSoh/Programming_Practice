def DFS_Recur(r, c, image, color, visited, floodVal):
        # Check for out of bounds
        rInbounds = (r >= 0) and (r < len(image))
        cInbounds = (c >= 0) and (c < len(image[0]))
        
        if not rInbounds or not cInbounds:
            return
        
        # If current cell val != val of the starting image, do nothing and return
        if image[r][c] != floodVal:
            return
        
        # Prevent infinite loops
        if f"{r},{c}" in visited:
            return
        
        visited.add(f"{r},{c}")
        
        # If current cell val == val of the starting image, flood the current cell with the color
        if image[r][c] == floodVal:
            image[r][c] = color

        # Go Up, Down, Right and Left
        DFS_Recur(r+1,c,image,color,visited,floodVal)
        DFS_Recur(r-1,c,image,color,visited,floodVal)
        DFS_Recur(r,c+1,image,color,visited,floodVal)
        DFS_Recur(r,c-1,image,color,visited,floodVal)
        
        return


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # If the starting cell has the same value as the flooding value, do nothing and return the original image
    if image[sr][sc] == color:
        return image
    # Else, flood the cells that have the same value as the starting cell
    visited = set()
    DFS_Recur(sr,sc,image,color,visited,image[sr][sc])
    return image

if __name__ == "__main__":
    image1 =  [[1,1,1],[1,1,0],[1,0,1]]
    # Starting position in image
    sr = 1
    sc = 1
    # Color to flood the cell that has the same value as the starting cell
    color = 2

    print(f"The resulting image1 after flooding with {color} is {floodFill(image1,sr,sc,color)}")

    image2 = [[0,0,0],[0,0,0]]
    print(f"The resulting image1 after flooding with {0} is {floodFill(image1,0,0,0)}")
