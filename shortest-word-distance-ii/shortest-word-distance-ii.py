# Create a map which is ready to get it index and then go to that particular list and
# caluculate there index!


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordMap = collections.defaultdict(list)
        
        for i in range(len(wordsDict)):
            self.wordMap[wordsDict[i]].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        numList1 = self.wordMap[word1]
        numList2 = self.wordMap[word2]
        minimum = float("inf")
        p1 = 0
        p2 = 0
        
        while p1 < len(numList1) and p2 < len(numList2):
            val1 = numList1[p1]
            val2 = numList2[p2]
            minimum = min(minimum, abs(val1 - val2)) 
            
          # using two pointer approach for [1,4] and [1,3] see the sowmya video explained very well
            if val1 < val2:
                p1 += 1
            else:
                p2 += 1
        return minimum
                
            
            
            
            
        
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)