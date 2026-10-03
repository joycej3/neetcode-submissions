class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_SIZE = len(board)
        COL_SIZE = len(board[0])
        def recursive(i,j,c):
            if c == len(word):
                return True
            

            if (i < 0 or i >= ROW_SIZE or j < 0 or j >= COL_SIZE or board[i][j] != word[c] or board[i][j] == '#'):
               return False

            board[i][j] = '#'
            res = (recursive(i+1, j, c+1) or
                        recursive(i-1, j, c+1) or 
                        recursive(i, j+1 ,c+1) or 
                        recursive(i, j-1 ,c+1))
            board[i][j] = word[c]
            return res
               


        for i  in range(ROW_SIZE):
            for j in range(COL_SIZE):
                if recursive(i,j, 0):
                    return True
        return False