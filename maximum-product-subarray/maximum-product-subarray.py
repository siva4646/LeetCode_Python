# Check link for maximum sum subarray and maximum product subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        result, global_min, global_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            local_min = global_min
            local_max = global_max
            global_max = max(max(nums[i], local_max * nums[i]), local_min * nums[i])
            global_min= min(min(nums[i], local_max * nums[i]), local_min * nums[i])
            result = max(result, global_max)
        return result
        