class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or len(tokens) == 0:
            return 0
        
        stack = []
        operators = {'+', '-','*','/'}
        for t in tokens:
            if t in operators:
                second = stack.pop()
                first = stack.pop()
                if t == '+':
                    stack.append(first + second)
                elif t == '-':
                    stack.append(first - second)
                elif t == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(t))
        return stack[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(tokens)):
        #     if tokens[i].isnumeric():
        #         stack.append(tokens[i])
        #     else:
        #         val = stack.pop()
        #         res = 
        # return stack
            
        