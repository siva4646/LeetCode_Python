class Solution:
    def maxScore(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        maxi = 0
        
        for i in range(1, len(s)):
            result = 0
            
            right = s[i:]
            left = s[:i]
            
            result = left.count("0") + right.count("1")
            maxi = max(result, maxi)
        
            # if result > maxi:
            #     maxi = result
        
        return maxi
        