# Time: O(N)
# Space: O(K) length of strings

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs or len(strs) == 0:
            return []
        
        dic = {}
        result = []
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in dic:
                dic[word_sorted] = [word]
            else:
                dic[word_sorted].append(word)
                
        for key,value in dic.items():
            result.append(value)
        return result