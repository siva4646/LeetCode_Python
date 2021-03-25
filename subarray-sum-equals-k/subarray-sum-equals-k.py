class Solution(object):
    def subarraySum(self, nums, k):
        if not nums or len(nums) == 0:
            return 0
        
        count = 0
        rSum = 0
        dic = {0:1}
        
        for i in range(len(nums)):
            rSum = rSum + nums[i]
            compliement = rSum - k
            
            if compliement in dic:
                count += dic[compliement]
                
            if rSum not in dic:
                dic[rSum] = 1
            else:
                dic[rSum] += 1
                
        return count
        