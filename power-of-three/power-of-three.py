class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return 0
        
        while n != 0:
            if n != 1 and n % 3 != 0:
                return False
            else:
                n = n // 3
                
        return True
        