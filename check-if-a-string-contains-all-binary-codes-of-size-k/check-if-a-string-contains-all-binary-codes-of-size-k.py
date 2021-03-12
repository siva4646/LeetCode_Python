class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        # We want the last slice of s, s[i:i+k] to be of length k
        for i in range(len(s)-k + 1):
            codes.add(s[i:i+k])
            # print(codes)
        if len(codes) == 2 ** k:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/661063/Python-4-lines-O(N)-with-explanation