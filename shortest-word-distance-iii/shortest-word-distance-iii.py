class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        minimum = float("inf")
        
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                index1 = i
                
            if word2 == wordsDict[i]:
                if index1 == i:
                    index1 = index2
                index2 = i
            
            if index1 != -1 and index2 != -1:
                minimum = min(minimum, abs(index2 - index1))
            
        return minimum
            
                
        