class Solution:
    def reorganizeString(self, S: str) -> str:
        if S == "" or len(S) == 0:
            return ""
        
        max_Heap = []
        dic = Counter(S)
        p_freq = 0
        p_char = ""
        result = []
        
        for key, value in dic.items():
            heapq.heappush(max_Heap, (-value, key))
            
        # heapq.heapify(max_Heap)
        
        while max_Heap:
            freq, char = heapq.heappop(max_Heap)
            result.append(char)
            
            if p_freq != 0:
                heapq.heappush(max_Heap, (p_freq, p_char))
                
            freq += 1
            p_freq, p_char = freq, char
            
        result = "".join(result)
        
        if len(result) != len(S):
            return ""
        return result
            
            