# Look for callable how it works
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix or len(matrix) == 0:
            return []
        
        for r in range(len(matrix)):
            for c in range(r, len(matrix)):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
                
        for r in range(len(matrix)):
            matrix[r].reverse()
    
        
            
                