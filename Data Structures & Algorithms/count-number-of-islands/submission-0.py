class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R_SIZE = len(grid)
        C_SIZE = len(grid[0])
        def dfs(i,j):
            stack = [(i,j)]

            while stack:
                curr_i, curr_j = stack.pop()
                grid[curr_i][curr_j] = "0"

                if curr_i - 1 >= 0 and grid[curr_i-1][curr_j] == "1":
                    stack.append((curr_i - 1, curr_j))
                if curr_j - 1 >= 0 and grid[curr_i][curr_j-1] == "1":
                    stack.append((curr_i, curr_j-1))
                if curr_i + 1 <R_SIZE  and grid[curr_i+1][curr_j] == "1":
                    stack.append((curr_i + 1, curr_j))
                if curr_j + 1 < C_SIZE  and grid[curr_i][curr_j+1] == "1":
                    stack.append((curr_i, curr_j+1))
            return 

        res = 0

        for i in range(R_SIZE):
            for j in range(C_SIZE):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res +=1
        return res 
