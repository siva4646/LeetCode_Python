class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #Sliding Window 
        left = 0
        right = 0
        rSum = 0
        rLen = float('inf')
        
        while left < len(nums):
            # Growth Phase
            if rSum < s:
                rSum += nums[left]
                left += 1
            # Shrink Phase
            while rSum >= s:
                if left - right  < rLen:
                    rLen = left - right
                    print(rLen)
                else:
                    rSum -= nums[right]
                    right += 1
                  
        if rLen == float('inf'): # not reached it says we are just growing phase which rlen never change
            return 0
        else:
            return rLen
        
#https://www.youtube.com/watch?v=SeJgBWg1_w4&ab_channel=Brevity-CodeIntuitively

#https://www.youtube.com/watch?v=giwV72VxEd8&ab_channel=Brevity-CodeIntuitively