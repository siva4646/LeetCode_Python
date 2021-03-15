class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        result = []
        for i in range(len(S)):
            dic[S[i]] = i
        print(dic)
            
        start_idx = 0
        end_idx = 0
 
        for i in range(len(S)):
            end_idx = max(end_idx, dic[S[i]])
            print(end_idx)
            if i == end_idx:
                result.append(i - start_idx + 1)
                start_idx = i + 1
        return result 