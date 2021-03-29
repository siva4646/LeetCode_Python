class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((0,0,1))
    
        directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        while queue:
            i, j , steps = queue.popleft()
            if i == m - 1 and j == n - 1:
                return steps
            for dirs in directions:
                r = dirs[0] + i
                c = dirs[1] + j
                if 0 <= r < m and 0<= c < n and not grid[r][c]: 
                    queue.append((r, c, steps + 1))
                    #print(queue)
                    grid[r][c] = "X"
        return -1
                
                    
        
        