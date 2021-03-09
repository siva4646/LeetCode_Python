# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time and Space: O(Nlogn) Since it sort in heap and O(N)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(minHeap,(lists[i].val, i, lists[i].next))
               
        dummy = ListNode(-1)
        curr = dummy
        
        while len(minHeap) != 0:
            value, index, node = heapq.heappop(minHeap)
            if node != None:
                heapq.heappush(minHeap, (node.val, index, node.next))
                
            curr.next = ListNode(value)
            curr = curr.next
            
        return dummy.next