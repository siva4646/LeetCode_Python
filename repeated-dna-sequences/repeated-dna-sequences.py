class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []
        
        resultSet = set()
        allSubSet = set()
        
        for i in range(len(s)):
            string = s[i:i+10]
            if string in allSubSet:
                resultSet.add(string)
            allSubSet.add(string)
        return resultSet