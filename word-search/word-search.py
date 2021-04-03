class Solution(object):
    def exist(self, board, word):
        if not board or len(board) == 0:
            return False
        self.row = len(board)
        self.col = len(board[0])
        
        for i in range(self.row):
            for j in range(self.col):
                if self.backtrack(board,word, i, j, 0):
                    return True
        return False
    
    def backtrack(self, board,word, i, j, index):
        # base case
        if len(word) == index:
            return True
        if i < 0 or j < 0 or i == self.row or j == self.col or board[i][j] == "#":
            return False
        
        # logic
        if board[i][j] == word[index]:
            temp = board[i][j]
            board[i][j] = "#"
            directions = [(-1,0), (1,0), (0, -1), (0,1)]
            
            for dirs in directions:
                r = dirs[0] + i
                c = dirs[1] + j
                if self.backtrack(board, word, r, c, index + 1):
                    return True
            board[i][j] = temp 
        return False
        
            
                