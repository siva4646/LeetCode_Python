class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        max_area = 0
        self.area = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    max_area = max(max_area, self.area)
                    self.area = 0
        return max_area
    
    def dfs(self, grid, i, j):
        # base case
        if i < 0 or j < 0 or i == self.m or j == self.n or grid[i][j] != 1:
            return 
        
        self.area += 1
        grid[i][j]= "X"
        
        dirs = [(0,1), (1,0), (-1, 0), (0,-1)]
        for d in dirs:
            r = d[0] + i
            c = d[1] + j
            self.dfs(grid, r, c)