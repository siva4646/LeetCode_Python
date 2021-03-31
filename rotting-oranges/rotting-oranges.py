class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        queue = deque()
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: #[[0]] Test case 
            return 0
        time = 0
        directions = [(-1,0),(1,0), (0,1),(0,-1)]
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                for dirs in directions:
                    r = dirs[0] + curr[0]
                    c = dirs[1] + curr[1]
                    if r >= 0 and c >= 0 and r < m and c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
                        fresh -= 1
            time += 1
            
        if fresh != 0:
            return -1
        return time - 1
        
                        
            
            