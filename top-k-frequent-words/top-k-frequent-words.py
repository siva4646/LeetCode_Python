class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or len(words) == 0:
            return words
        
        dic = {}
        maxHeap = []
        result = []
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        
        for key, value in dic.items():
            heapq.heappush(maxHeap, (-value, key))
        
        while k != 0:
            result.append(heapq.heappop(maxHeap)[1])
            k -= 1
        return result