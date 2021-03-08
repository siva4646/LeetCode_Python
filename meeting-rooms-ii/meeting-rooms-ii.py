class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        freeRoom = []
        intervals.sort(key = lambda x:x[0])
        heapq.heappush(freeRoom, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if freeRoom[0] <= intervals[i][0]:
                heapq.heappop(freeRoom)
            heapq.heappush(freeRoom, intervals[i][1])
        return len(freeRoom)
                
        

   






    #https://www.youtube.com/watch?v=9ZsUM1ed05c&ab_channel=CodingWithJaz
        