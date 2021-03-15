class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        
        for i in range(len(nums)):
            next_idx = abs(nums[i]) - 1
            if nums[next_idx] > 0:
                nums[next_idx] *= -1
            else:
                return next_idx + 1
            
                
        