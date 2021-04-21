class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        arr = [0 for i in range(len(nums) + 1)]
        
        nt_choose, choose = 0 , 0
        for i in nums:
            nt_choose, choose = max(nt_choose, choose) , i + nt_choose
        return max(nt_choose, choose)
            