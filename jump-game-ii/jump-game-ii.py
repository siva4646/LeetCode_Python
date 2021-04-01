class Solution:
    def jump(self, nums: List[int]) -> int:
        maxdest = float("-inf")
        pos = 0
        jump = 0
        for i in range(len(nums) - 1):
            maxdest = max(maxdest, i + nums[i])
            
            if pos == i:
                pos = maxdest
                jump += 1
                
        if pos >= len(nums)- 1:
            return jump
        return 0
        