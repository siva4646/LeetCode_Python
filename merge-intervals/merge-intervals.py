class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x:x[0])
        result = []
        for char in intervals:
            if result and char[0] <= result[-1][1]:
                result[-1][1] = max(char[1], result[-1][1])
            else:
                result.append(char)
                
        return result