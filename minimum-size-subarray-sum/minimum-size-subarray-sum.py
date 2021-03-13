class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        rSum = 0
        rLen = float("inf")
        
        while left < len(nums):
            if rSum <= s:
                rSum = rSum + nums[left]
                left += 1
            
            while rSum >= s:
                if left - right <= rLen: 
                    rLen = left - right
                    
                rSum = rSum - nums[right]
                right += 1

        if rLen == float("inf"):
            return 0
        else:
            return rLen
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#https://www.youtube.com/watch?v=SeJgBWg1_w4&ab_channel=Brevity-CodeIntuitively

#https://www.youtube.com/watch?v=giwV72VxEd8&ab_channel=Brevity-CodeIntuitively