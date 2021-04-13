class Solution:
    def jump(self, nums: List[int]) -> int:
        maxdest = float("-inf")
        pos = 0
        jump = 0
        for i in range(len(nums) - 1):
            # calculate the max dest from the index 
            maxdest = max(maxdest, i + nums[i])
            
            # will get with min jump to reach destination
            if pos == i:
                pos = maxdest
                jump += 1
                
        #if pos >= len(nums)- 1:
        return jump
        #return 0
        