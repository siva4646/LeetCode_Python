class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1]* n for i in range(m)]
        
        for col in range(1, m):
            for row in range(1,n):
                dp[col][row] = dp[col-1][row] + dp[col][row-1]
        return dp[m-1][n-1]