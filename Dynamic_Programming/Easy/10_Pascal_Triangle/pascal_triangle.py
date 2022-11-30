# The start and end of the pascal's triangle row is always 1.
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

def generate(numRows: int) -> list[list[int]]:
    # Always starts with a 1
    triangle = [[1]]
    
    # For each level, sum the prevRow's numbers at index i-1 and i and append it to the currRow.
    for row in range(1,numRows):
        currRow = []
        prevRow = triangle[row-1]
        # Start = 1
        currRow.append(1)
        # Sum the numbers in the previous row at index i-1 and i for the pascal's triangle currRow.
        for i in range(1,len(prevRow)):
            # print(currRow)
            currRow.append(prevRow[i-1] + prevRow[i])
        # End = 1
        currRow.append(1)
        triangle.append(currRow)
    
    return triangle


if __name__ == "__main__":
    numRows1 = 5
    print(f"The Pascal's Triangle values for triangle is {generate(numRows1)}")
    numRows2 = 1
    print(f"The Pascal's Triangle values for triangle is {generate(numRows2)}")
