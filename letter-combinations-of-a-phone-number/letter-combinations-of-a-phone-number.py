class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #Backtracking return all possible letter combinations that the number could represent.
        #Since we are exhausing all possible values. 
        
        if len(digits) == 0:
            return []
        
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': "pqrs", '8': "tuv", '9': "wxyz"}
        
        result = []
        string = ""
        self.backtrack(result, phone, string, 0, digits)
        return result
    
    def backtrack(self, result, phone, string, index, digits):
        # base condition or stopping condition
        if len(digits) == len(string): #EX: 23 -> ab 
            result.append(string)
            return 
        
        letters = phone[digits[index]]
        for char in letters:
            #action
            string += char
            #recurse
            self.backtrack(result, phone, string, index + 1, digits)
    # backtrack(go back and nullfiing the answer) [CHECK removing it and print statement]
            string = string[:-1]
        