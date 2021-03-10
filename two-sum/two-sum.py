class Solution(object):
    def twoSum(self, nums, target):
        if not nums or len(nums) == 0:
            return []
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                return dic[nums[i]],i
      
            
            
            
            
    
        