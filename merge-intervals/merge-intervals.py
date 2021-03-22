class Solution(object):
    def merge(self, intervals):
        if not intervals or len(intervals) == 0:
            return []
        
        result = []
        intervals.sort(key = lambda x:x[0])
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
        return result
        