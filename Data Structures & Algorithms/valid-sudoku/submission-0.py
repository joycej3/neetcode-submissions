class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        square = defaultdict(set)
        col = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                square_i = 1+ j //3 + (i//3)*3 
                if curr in row[i] or curr in col[j] or curr in square[square_i]:
                    return False
                row[i].add(curr)
                col[j].add(curr)
                square[square_i].add(curr)
        return True