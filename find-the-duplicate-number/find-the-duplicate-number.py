class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            new_Index = abs(nums[i])
            if nums[new_Index] > 0:
                nums[new_Index] *= -1
                #print(nums)
            else:
                return new_Index 
        