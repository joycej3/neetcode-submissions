class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R_SIZE, C_SIZE = len(board), len(board[0])    
        def check(i,j,c):
            if c == len(word):
                return True

            if i < 0 or j < 0 or i >= R_SIZE or j >= C_SIZE or board[i][j] != word[c] or board[i][j] == '#':
                return False


            board[i][j] = '#'
            res = (check(i+1, j, c+1) or
                check(i-1, j, c+1) or
                check(i, j+1, c+1) or
                check(i, j-1, c+1))
            board[i][j] = word[c]
            return res




        for i in range(R_SIZE):
            for j in range(C_SIZE):
                if check(i,j,0) == True:
                    return True
        return False




