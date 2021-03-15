# Testcase: "){" , "()[]{}" 
class Solution:
    def isValid(self, s: str) -> bool:
        #base case with odd form
        if s == 0 or len(s) % 2 != 0:
            return False
        
        stack = []
        dic = { ')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char in dic:
                if not stack or dic[char] != stack.pop():
                    return False
            else:
                stack.append(char)
                
        if not stack:
            return True
        return False
         
        

                
                
        
         