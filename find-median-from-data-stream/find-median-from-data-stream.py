# Time and Space Complexity: O(log n) and O(n)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        maxHeap = self.maxHeap
        minHeap = self.minHeap
        if len(maxHeap) == 0 or num < -maxHeap[0]:
            heapq.heappush(maxHeap, -num)
           
        else:
            heapq.heappush(minHeap, num)
        #print(maxHeap, minHeap)
        if len(maxHeap) - len(minHeap) >= 2:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif len(minHeap) - len(maxHeap) >= 2:
            heapq.heappush(maxHeap, -heappop(minHeap))
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        # if even number in both minHeap and maxHeap
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        # if odd number then just remove from minHeap if len(minHeap) > len(maxHeap)
        elif len(self.minHeap) > len(self.maxHeap): # [2,3] [-1]
            return self.minHeap[0]
        else:
            return -self.maxHeap[0] # [3] [-1,-2]
        

#https://www.youtube.com/watch?v=EcNbRjEcb14&ab_channel=KeertiPurswani
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()