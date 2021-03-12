class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return nums
        
        result = []
        rSum = 0
        for i in range(len(nums)):
            rSum = rSum + nums[i]
            result.append(rSum)
        return result