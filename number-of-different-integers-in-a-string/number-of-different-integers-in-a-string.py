class Solution(object):
    def numDifferentIntegers(self, word):
        nums, token = set(), ""
        
        for i, char in enumerate(word):
            if token != "" and char.isalpha():
                nums.add(int(token))
                token = ""
            elif char.isdigit():
                token += char
                
            if i == len(word) - 1 and char.isdigit():
                nums.add(int(token))
            
        return len(nums)
        