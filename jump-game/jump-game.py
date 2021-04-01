class Solution(object):
    def canJump(self, nums):
        maxdest = float("-inf")
        pos = 0
        
        for i in range(len(nums) - 1):
            maxdest = max(maxdest, i + nums[i])
            
            if pos == i:
                pos = maxdest
                
        if pos >= len(nums) - 1:
            return True
        return False
        