class Solution:
    def heightChecker(self, heights: List[int]) -> int:        
        expHeight = sorted(heights)
        if heights == expHeight:
            return 0
        
        count = 0
        for i in range(len(heights)):
            if heights[i] != expHeight[i]: #> expHeight[i] or heights[i] < expHeight[i]:
                count += 1
        return count
        