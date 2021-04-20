class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxi = max(nums)
        
        arr = [0 for i in range(maxi +1)]

        for i in nums:
            arr[i] += i
            
        nt_choose, choose = 0, 0
        for i in arr:
            nt_choose, choose = max(nt_choose, choose), i + nt_choose
        return max(nt_choose, choose)
            
        