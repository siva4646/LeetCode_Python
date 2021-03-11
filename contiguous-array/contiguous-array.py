class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dic = {0: -1}
        rSum = 0
        lenthSubArray = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                rSum -= 1
            else:
                rSum += 1
            
                
            if rSum in dic:
                lenthSubArray = max(lenthSubArray, i - dic[rSum])
            else:
                dic[rSum] = i
                
        return lenthSubArray
        
          