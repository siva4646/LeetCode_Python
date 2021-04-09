class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        result = []
        capacity = s.count(')')
        opened = 0
        for char in s:
            if char == '(':
                if opened == capacity: continue #Python returns the control to the beginning of the while loop
                opened += 1
            elif char == ')':
                capacity -= 1
                if not opened: continue #In summary, we can use if not expression to conditionally execute a block of statements only if the value is not empty or not False.
                opened -= 1 
            # print(result)
            result.append(char)
        return ''.join(result)
    
    
#https://stackoverflow.com/questions/16739555/python-if-not-syntax
                
                
        
        
                
        
        