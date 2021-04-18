class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        rSum = 0
        count = 0
        for cost in costs:
            rSum = rSum + cost
            if rSum <= coins:
                count += 1       
        return count
            #     count += 1
            # else:
            #     rSum = rSum - cost
            #rSum = rSum + cost
          
             # if rSum <= coins:
             #    count += 1
        # return count 