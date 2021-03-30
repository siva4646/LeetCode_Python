# DP Solution
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        maxi = 1
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxi = max(maxi, dp[i])
                    
        return maxi
        