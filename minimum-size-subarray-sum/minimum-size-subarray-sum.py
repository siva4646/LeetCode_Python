class Solution(object):
    def minSubArrayLen(self, target, nums):
        rSum = 0
        left = 0
        right = 0
        rLen = float("inf")
        
        while left < len(nums):
            if rSum < target:
                rSum = rSum + nums[left]
                left += 1
                
            while rSum >= target:
                if left - right < rLen:
                    rLen = left - right
                else:
                    rSum = rSum - nums[right]
                    right += 1
                    
        if rLen == float("inf"):
            return 0
        return rLen
                
            
        