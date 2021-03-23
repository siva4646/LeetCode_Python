class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0:
            return 0
        
        result = 0 
        maxi = 0
        
        for index, num in enumerate(arr):
            maxi = max(maxi, num)
            if index == maxi:
                result += 1
        return result
        