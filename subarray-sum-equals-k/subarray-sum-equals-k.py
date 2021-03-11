
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #running sum
        if not nums or len(nums) == 0:
            return 0
        
        dic = {0: 1}
        count = 0
        rSum = 0
        for i in range(len(nums)):
            rSum += nums[i]
            compliment = rSum - k
            if compliment in dic:
                count += dic[compliment]
               
            if rSum not in dic:
                dic[rSum] = 1
            else:
                dic[rSum] += 1
        return count