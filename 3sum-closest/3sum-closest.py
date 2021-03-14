class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
 
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(result - target):
                    result = total
                if total < target:
                    left += 1
                else:
                    right -= 1
                
        return result