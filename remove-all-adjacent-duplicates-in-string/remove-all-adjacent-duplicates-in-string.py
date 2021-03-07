class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S or len(S) == 0:
            return S
        
        stack = []
        for i in range(len(S)):
            if stack and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return "".join(stack)
        