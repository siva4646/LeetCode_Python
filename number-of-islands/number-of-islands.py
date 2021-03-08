class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, i, j):
        # Base
        if i < 0 or j < 0 or i == self.m or j == self.n or grid[i][j] != "1":
            return 
        # Logic
        grid[i][j] = "X"
        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        for dirs in direction:
            r = dirs[0] + i
            c = dirs[1] + j
            self.dfs(grid, r, c)