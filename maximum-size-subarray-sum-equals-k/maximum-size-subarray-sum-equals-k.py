class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        dic = {0: -1}
        max_length = 0
        rSum = 0
        for i in range(len(nums)):
            rSum += nums[i]
            compliment = rSum - k
            if compliment in dic:
                max_length = max(max_length, i - dic[compliment])
                
            if rSum not in dic:
                dic[rSum] = i
    
        return max_length 
                
        