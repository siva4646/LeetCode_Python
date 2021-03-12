class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == None:
            return 0
        rSum = nums[0]
        maxi = nums[0]
        
        for i in range(1, len(nums)):
            rSum = max(rSum + nums[i], nums[i]) # current array
            maxi = max(rSum, maxi) # global array one 
        return maxi 