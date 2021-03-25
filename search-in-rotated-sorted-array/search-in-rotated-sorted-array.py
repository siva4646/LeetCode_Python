class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low +(high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] >= target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
                    