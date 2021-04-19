class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapTopElement = defaultdict(list)
        
        for Id, score in items:
            heapq.heappush(mapTopElement[Id], -score)
        
        result = []
        for key in mapTopElement:
            total = 0
            count = 5
            
            while count > 0:
                heapElemnts = heapq.heappop(mapTopElement[key])
                total = total - heapElemnts 
                count -= 1
                
            result.append([key, total//5 ])
            result.sort()   
        return result
        