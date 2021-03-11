class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s or len(s) == 0:
            return -1
        
        # if you use counter it will be in same order as the input string
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1
            
        
    