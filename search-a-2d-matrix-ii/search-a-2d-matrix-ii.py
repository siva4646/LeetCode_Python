#Time Complexity: O(n + m)
#Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        row = 0
        col = width - 1
        
        while row < height and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False
        