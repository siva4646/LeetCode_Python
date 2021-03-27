from heapq import heappush as insert
from heapq import heappop as remove
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hashset = set()
        heap = []
        heapq.heappush(heap, 1)
        hashset.add(1)
        
        for i in range(n-1):
            curr = remove(heap)
            n2 = 2 * curr
            n3 = 3 * curr
            n5 = 5 * curr
            if n2 not in hashset:
                hashset.add(n2)
                insert(heap, n2)
            if n3 not in hashset:
                hashset.add(n3)
                insert(heap, n3)
            if n5 not in hashset:
                hashset.add(n5)
                insert(heap, n5)
        return remove(heap)
         
        