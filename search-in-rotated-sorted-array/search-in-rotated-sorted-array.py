class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left+ (right - left) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1
            else:
                if nums[right] >= target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1 
        