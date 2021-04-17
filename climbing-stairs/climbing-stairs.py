# See Back to Back SWE Explanied so well!
class Solution(object):
    def climbStairs(self, n):
#         return self.climb_Stairs(0, n)
    
#     def climb_Stairs(self, index, n):
#         # base
#         if index > n:
#             return 0
#         if index == n:
#             return 1
#         # recurse
#         return self.climb_Stairs(index+1, n) + self.climb_Stairs(index+2, n)
       
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        