class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        expected_sum = length * (length + 1) // 2
        total_sum = sum(nums)
        result = expected_sum - total_sum
        return result
        