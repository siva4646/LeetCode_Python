class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
    
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i- 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # to get unique tripet
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    
                    left = left + 1
                    right = right - 1
                    
        return result 
                    
        
        