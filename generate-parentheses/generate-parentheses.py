class Solution(object):
    def generateParenthesis(self, n):
        result = []
        string = ""
        self.backtrack(string, n, 0, 0, result)
        return result
    
    def backtrack(self, string, n, openBracket, closeBracket, result):
        if openBracket == n and closeBracket == n:
            result.append(string)
            
        if openBracket < n:
            self.backtrack(string + '(', n, openBracket + 1, closeBracket, result)
            
        if closeBracket < openBracket:
            self.backtrack(string + ')', n, openBracket, closeBracket + 1, result)
        