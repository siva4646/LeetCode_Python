class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            newIndex = abs(n)- 1
            if nums[newIndex] > 0:
                 nums[newIndex] *= -1
            else: 
                res.append(abs(n))
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for i in range(len(nums)):
#             index = nums[i]
#             print(index)
#             if index == len(nums):
#                 nums[0] = -1
            
#             elif nums[index] != -1:
#                 nums[index] = -1
#             #print(nums)
#         res = []
#         for n in nums:
#             if n != -1:
#                 res.append(n)
        
#         return res
            