class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dest = float("-inf")
        pos = 0
        
        for i in range(len(nums) - 1):
            # calculate the max dest from that index
            max_dest = max(max_dest, i + nums[i])
            
            # will get with min jump to reach destination
            if pos == i:
                pos = max_dest
        
        if pos >= len(nums) -1:
            return True
        return False
        
        
        
        