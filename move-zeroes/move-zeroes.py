class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return []
        
        left = 0
        right = 0
        
        while left < len(nums):
            if nums[left] == 0:
                left += 1
            else:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1
        return nums