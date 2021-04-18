# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        fast = dummyNode
        slow = dummyNode
        count = 0
        
        while count <= n:
            fast = fast.next
            count += 1
        #print(fast.val)
            
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummyNode.next 
            
        