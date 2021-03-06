class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 0:
            return []
        
        dic = collections.defaultdict(list)
        result = []
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
                
        for key, items in dic.items():
            result.append(items)
        return result
        