# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None or not head:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        for i in range(1, left):
            prev = prev.next
        
        curr = prev.next 
        
        for i in range(left, right):
            next_point = curr.next
            curr.next = next_point.next
            next_point.next = prev.next
            prev.next = next_point
            
        return dummy.next
            
        