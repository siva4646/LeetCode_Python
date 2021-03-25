class Solution(object):
    def isMatch(self, s, p):
        if s == p or p == "*":
            return True
        sStar, pStar= -1, -1
        sp, pp = 0, 0
        
        while sp < len(s):
            # case 1
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == "*": # Zero case
                pStar = pp
                sStar = sp
                pp += 1
            elif pStar == -1:
                return False
            else:
                sStar += 1
                sp = sStar
                pp = pStar + 1
                
        while pp < len(p):
            if p[pp] != "*":
                return False
            pp += 1
        return True
            
        