class Solution(object):
    def removeDuplicates(self, s, k):
        if not s or len(s) == 0:
            return ""
        
        stack = [["*",0]]

        for char in s:
            if char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
                
        return "".join([char * times for char, times in stack])
                