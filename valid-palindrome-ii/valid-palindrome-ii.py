class Solution:
    def validPalindrome(self, s: str) -> bool:
        # start scanning from both ends
        # you can skip at most 1 char
        
        if not s:
            return True
        
        start = 0
        end = len(s) - 1
        
        def isValid(start, end, skipped):
            if skipped > 1:
                return False
            
            if start >= end:
                return True
            
            if s[start] == s[end]:
                return isValid(start+1, end-1, skipped)
            else:
                return isValid(start, end-1, skipped+1) or isValid(start+1, end, skipped+1)
        
        return isValid(start, end, 0)
        