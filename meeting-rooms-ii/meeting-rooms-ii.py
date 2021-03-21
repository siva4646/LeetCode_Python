class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x:x[0])
        # minHeap
        freeRoom = []
        heapq.heappush(freeRoom, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if freeRoom[0] <= intervals[i][0]:
                heapq.heappop(freeRoom)
            heapq.heappush(freeRoom, intervals[i][1])
        return len(freeRoom)