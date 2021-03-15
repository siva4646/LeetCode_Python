class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s or not cost:
            return 0
        slow=0
        result=0
        l=len(s)
        for j in range(1,l+1):
            if j>=l or s[j]!=s[slow]:
                if j-slow>1:
                    sum_=sum(cost[slow:j])
                    max_=max(cost[slow:j])
                    result+=sum_-max_
                slow=j
        return result