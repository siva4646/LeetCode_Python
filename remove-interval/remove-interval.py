class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        result = []
        for start, end in intervals:
            if start > remove_end or end < remove_start:
                result.append([start, end])
            else:
                if start < remove_start:
                    result.append([start, remove_start])
                
                if end > remove_end:
                    result.append([remove_end, end])
                    
        return result
        
        
        
    
    
    
    
    
    
    
        
#         intervals.sort(key = lambda x:x[0])
#         result = []
#         result.append(intervals[0])
#         for i in range(len(toBeRemoved)):
#             if toBeRemoved[0] < result[-1][1]:
#                 result[-1][1] = min(toBeRemoved[0], result[-1][1])
        
#         last_element = len(intervals) - 1
#         result.append(intervals[last_element])
        
#         for i in range(len(toBeRemoved)):
#             if toBeRemoved[1] > result[-1][0]:
#                 result[-1][0] = max(toBeRemoved[1], result[-1][0])
        
#         return result
        