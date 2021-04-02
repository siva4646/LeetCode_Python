class Solution(object):
    def gameOfLife(self, board):
        # 1 -> 0 2
        # 0 -> 1 3
        if not board or len(board) == 0:
            return 
        
        m = len(board) 
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                count = self.countLives(board, i, j)
                # Rule 1 and 3
                if (board[i][j] == 1 and (count < 2 or count > 3)):
                    board[i][j] = 2
                # Rule 4
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
                    
    def countLives(self, board, i, j):
        count = 0
        directions = [(-1,0), (0, -1), (0,1), (1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

        for dirs in directions:
            r = dirs[0] + i
            c = dirs[1] + j

            if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]) and (board[r][c] == 1 or board[r][c] == 2):
                count += 1
        
        return count 
                    
        