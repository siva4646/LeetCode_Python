class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or len(words) == 0:
            return words
        
        max_heap = []
        dic = {}
        result = []
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        
        for key, value in dic.items():
            heapq.heappush(max_heap, (-value, key))
            
        while k != 0:
            result.append(heapq.heappop(max_heap)[1])
            k -= 1
        return result