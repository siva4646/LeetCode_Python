class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals or len(intervals) == 0:
        #     return []
        
        result = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])      
        
        for char in intervals:
            if result and char[0] <= result[-1][1]:
                result[-1][1] = max(char[1], result[-1][1])
            else:
                result.append(char)
        return result
        