# Understand the Recursive call clearly in video!

# YOU NEED TO GIVE 3 SOLUTION N^2 , Bottom up with memoization T & S O(N) and iterative top down approach O(N) and O(1) V.V.V Important 



class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)
    
    def memoize(self, N):
        cache = {0: 0, 1: 1}
        
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[N]