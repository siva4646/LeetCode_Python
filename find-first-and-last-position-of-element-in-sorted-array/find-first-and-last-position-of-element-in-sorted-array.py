class Solution:
    def searchLeft(self, nums, target):
        low = 0 
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                if mid == low or nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    high = mid - 1
                    
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
    
    def searchRight(self, nums, target):
        low = 0 
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                if mid == high or nums[mid] < nums[mid + 1]:
                    return mid
                else:
                    low = mid + 1
                    
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
  
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return [left, right]
        