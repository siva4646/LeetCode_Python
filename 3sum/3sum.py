class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # it should not contain duplicate triplet
            # [-3, -3, 1,2,3,4] since -3 once visited so we will skip it continue or else we will lead same triplet
            if i > 0 and nums[i] == nums[i-1]:
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
                    # print(result)
                    # [-2, -2 , 0, 0,2,2] we don't have to have same number so left += 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 # right pointer will take care in first while loop
                        #[-2, -2 , 0, 0,2,2]
                    
        return result 
    
                    
        
        
