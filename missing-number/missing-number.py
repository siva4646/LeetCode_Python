class Solution(object):
    def missingNumber(self, num):
        missing = len(num)
        for i, num in enumerate(num):
            missing ^= i ^ num
        return missing
        