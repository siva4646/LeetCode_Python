class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p or p == "*":
            return True # Ex: 2
        sp , pp = 0,  0
        sStar, pStar = -1, -1
        
        while sp < len(s):
            #case 1 
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == "?"): # since increase pp+ = 1 check pp < pl 
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == "*": 
                 # Zero case
                sStar = sp
                pStar = pp
                pp += 1
            elif pStar == -1:
                return False
            else:  # One case
                sStar += 1
                sp = sStar # we skipped the char sStar or we cleverly matched that char to our *
                pp = pStar + 1
                
        while pp < len(p):
            if p[pp] != '*':
                return False
            pp += 1
        return True
            
                
                
            
        