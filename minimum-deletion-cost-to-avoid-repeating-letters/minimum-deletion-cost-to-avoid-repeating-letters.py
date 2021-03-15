class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        left = 0
        result = 0
        
        while left < len(s):
            right = left + 1
            maxCost = cost[left]
            curr = cost[left]
            
            while right < len(s) and s[left] == s[right]:
                maxCost = max(maxCost, cost[right])
                curr += cost[right]
                right += 1
                
            result += curr - maxCost
                
            left= right
        return result