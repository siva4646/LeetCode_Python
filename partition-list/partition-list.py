# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(-1)
        after = after_head = ListNode(-2)
        
        while head != None: #or head.next != None:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
            
        # before = after.next
        # return before
        
        after.next = None
        before.next = after_head.next
        return before_head.next
            
        