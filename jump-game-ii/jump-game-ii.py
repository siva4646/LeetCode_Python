class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_dest = float("-inf")
        pos = 0
        jump = 0
        for i in range(len(nums)-1):
            max_dest = max(max_dest, i + nums[i])
            
            if pos == i:
                pos = max_dest
                jump += 1
        
        return jump
        