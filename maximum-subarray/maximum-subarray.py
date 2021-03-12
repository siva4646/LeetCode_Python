# sliding window rSum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        rSum = nums[0]
        maxi = nums[0] # gobal array 
        
        start_idx = 0
        end_idx = 0
        startCurr = 0
        
        for i in range(1, len(nums)):
            rSum = rSum + nums[i]
            if rSum <= nums[i]:
                rSum = nums[i] #   rSum = max(rSum + nums[i], nums[i]) same doing this & above line
                startCurr = i
                # print(startCurr)
                #print("first", rSum, startCurr)
            
            if maxi <= rSum:
                maxi = rSum # maxi = max(maxi, rSum) same doing this and above line
                start_idx = startCurr
                print(start_idx)
                end_idx = i
                #print("second", maxi, start_idx, end_idx)
                
        print(start_idx, end_idx)
        return maxi