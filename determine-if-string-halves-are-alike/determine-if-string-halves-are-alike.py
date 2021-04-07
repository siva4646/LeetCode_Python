class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if not s or len(s) == 0:
            return False
        
        map_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        sLen = len(s)
        evenLen = len(s) // 2
        
        a = s[:evenLen]
        b = s[evenLen: sLen]
        countA = 0
        countB = 0
        for i in range(len(a)):
            if a[i] in map_set:
                countA += 1
            if b[i] in map_set:
                countB += 1
        
        if countA == countB:
            return True
        else:
            return False
            
            
        

        