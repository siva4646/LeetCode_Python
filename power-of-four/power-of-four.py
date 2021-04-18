class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return 0
        
        while n != 0:
            if n != 1 and n % 4 != 0:
                return False
            else:
                n = n//4
        return True
            
        