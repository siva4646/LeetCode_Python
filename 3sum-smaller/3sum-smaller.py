class Solution(object):
    def threeSumSmaller(self, nums, target):
        if not nums or len(nums) == 0:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums)- 1):
            p1 = i+ 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                total = nums[i] + nums[p1] + nums[p2]
                
                if total < target:
                    count += p2 - p1
                    p1 += 1
                else:
                    p2 -= 1
                    
        return count
                    
            
        