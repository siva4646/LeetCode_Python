# SEE THE LINK IN THE NOTES

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        d1 = dummy = ListNode(0)
        dummy.next = head
        
        while dummy.next and dummy.next.next:
            p = dummy.next
            q = dummy.next.next
            dummy.next = q
            p.next = q.next
            q.next = p
            #assign value of p to dummy
            dummy = p
        return d1.next
        