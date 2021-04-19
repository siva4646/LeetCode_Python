class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prevSeat = None
        dist = float("-inf")
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if prevSeat == None: # tells we are in first seat
                    dist = i
                else:
                    dist = max(dist, (i - prevSeat) // 2)
                prevSeat = i
        
        dist = max(dist, len(seats) - 1 - prevSeat)
        
        return dist
        