class Solution:
    def canJump(self, nums: List[int]) -> bool:
    
        max_dest = float("-inf")
        pos = 0
        for i in range(len(nums)-1):
            max_dest = max(max_dest, i + nums[i])
            
            if pos == i:
                pos = max_dest
        
        return pos >= len(nums)-1
            
        
        
        
        