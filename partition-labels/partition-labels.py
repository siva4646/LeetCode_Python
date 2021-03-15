class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        result = []
        for i in range(len(S)):
            dic[S[i]] = i
       
        start_idx = 0
        end_idx = 0
        
        for i in range(len(S)):
            end_idx = max(end_idx, dic[S[i]])
            if i == end_idx:
                result.append(i - start_idx + 1)
                start_idx = i + 1
        return result