# Array is sorted then think of Binary Search

class Solution(object):
    def missingNumber(self, arr):
        n = len(arr)
        
        diff = (arr[len(arr) - 1] - arr[0]) // n
        
        expected = arr[0]
        
        for val in arr:
            if val != expected:
                return expected
            
            expected += diff
            
        return expected
        
        
        