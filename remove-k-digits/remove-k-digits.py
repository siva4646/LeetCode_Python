class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or len(num) == 0:
            return ""
             
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        result = "".join(stack[:len(stack)-k]).lstrip('0')
        
        if len(result) != 0:
            return result
        else:
            return "0"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if stack and stack[-1] > num[i]:
        #         stack.pop()
        #     else:
        #         stack.append(num[i])
        #         print(stack)
        # return "".join(stack)
        