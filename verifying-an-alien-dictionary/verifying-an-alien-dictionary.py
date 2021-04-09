class Solution:
    def isAlienSorted(self, words, order):
        if not words or len(words) == 0:
            return True
        self.charMap = {}
        
        for i in range(26):
            self.charMap[order[i]] = i
            
        print(self.charMap)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            if self.isNotSorted(word1, word2): # if this is true it will go inside the and return false as final output
                return False
        return True
    
    def isNotSorted(self, word1, word2):
        p1 = 0
        p2 = 0
        
        while p1 < len(word1) and p2 < len(word2):
            char1 = word1[p1]
            char2 = word2[p2]
            
            if char1 != char2:
                return self.charMap[char1] > self.charMap[char2]
            
            p1 += 1
            p2 += 1
            
        return len(word1) > len(word2) #ex: [apple, app] apple > app so not sorted and return false