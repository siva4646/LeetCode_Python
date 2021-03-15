#why int(n/2) instead of n//2
#-1 // 2 = -1, so we would probably end up in ∞ loop but int(-1/2) is 0
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base
        if (n == 0):
            return 1
        
        temp = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return temp * temp
        elif n < 0:
            return temp * temp * (1/x)
        else:
            return temp * temp * x
