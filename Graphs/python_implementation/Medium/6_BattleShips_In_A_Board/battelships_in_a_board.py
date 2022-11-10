def countBattleships(board: list[list[str]]) -> int:
        count = 0
        def DFS_Recur(r,c,board):
            # If out of bounds or "."
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or board[r][c] != "X":
                return
            
            # If it is a battleship, we make sure its surrounding cells are all made to be "." as the conditions specified that a valid battleship must be separated by at 1 horizontal or vertical cell to other battleships.
            # - doing this will make sure we will not revisit it again.
            board[r][c] = "."
            
            DFS_Recur(r-1,c,board)
            DFS_Recur(r+1,c,board)
            DFS_Recur(r,c-1,board)
            DFS_Recur(r,c+1,board)
            
            return
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "X":
                    count += 1
                    DFS_Recur(r,c,board)
                
        return count

# The smart way to do it
def countBattleships_Smart(board : list[list[str]]) -> int:
    numBattleships = 0
    # Because we're scanning the board from top -> bot and left -> right, we're gonna check if the current battleship's top and left cells are battleship or not.
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == ".":
                continue
            # If the previous horizontal cell from the current 'r',c is a battleship, skip
            if r > 0 and board[r-1][c] == "X":
                continue
            # If the previous vertical cell from the current r,'c' is a battleship, skip
            if c > 0 and board[r][c-1] == "X":
                continue
            numBattleships += 1

    return numBattleships

if __name__ == "__main__":
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(f"How many battleships are in board 1 ? {countBattleships(board)}")
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(f"(Smart) How many battleships are in board 1 ? {countBattleships_Smart(board)}")
    
    board2 = [["."]]
    print(f"How many battleships are in board 2 ? {countBattleships(board2)}")
    board2 = [["."]]
    print(f"(Smart) How many battleships are in board 2 ? {countBattleships_Smart(board2)}")