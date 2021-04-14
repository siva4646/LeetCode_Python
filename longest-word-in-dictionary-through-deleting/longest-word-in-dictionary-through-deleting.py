# Check notes
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for dic_val in dictionary:
            if self.isSubsequence(s, dic_val):
                if len(dic_val) > len(result):
                    result = dic_val
                elif len(dic_val) == len(result) and dic_val < result:
                    result = dic_val
                    
        return "" if result is None else result
    
    def isSubsequence(self, S, D):
        pS = 0 # i
        pD = 0 # j
        while pS < len(S) and pD < len(D):
            if S[pS] == D[pD]:
                pS += 1
                pD += 1
            else:
                pS += 1
                    
        return pD == len(D)