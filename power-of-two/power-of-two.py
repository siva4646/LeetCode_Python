class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return 0
        
        while n != 0:
            if n != 1 and n % 2 != 0:
                return False
            else:
                n = n // 2
        return True
        