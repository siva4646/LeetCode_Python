class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        rSum = nums[0]
        maxi = nums[0]
        
        for i in range(1, len(nums)):
            #rSum = rSum + nums[i]
            rSum = max( rSum + nums[i], nums[i])
            maxi = max(maxi, rSum)
            
        return maxi
            