class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        topK = []
        for num in nums:
            heapq.heappush(topK, num)
            
            if len(topK) > k:
                heapq.heappop(topK)
                
        return topK[0]
            

        
        
        
        
        
        
        
        
        
        
             
        

        #https://www.youtube.com/watch?v=htqsw5NQMo4&ab_channel=jayatitiwari
#         if len(nums) == 0:
#             return 0
    
#         return heapq.nlargest(k, nums)[-1]
    
    
    #https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
    
    #https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/813237/Python-3-%2B-Heap-Explanation
    
    
        