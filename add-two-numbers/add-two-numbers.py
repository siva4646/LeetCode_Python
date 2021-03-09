# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next\

# See Note
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        # head to hold a initial node of l3
        head = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
                
            l3.val = carry % 10 # keep right val of 16(that is 6) gives reminder
            carry = carry // 10 # keep left val of 16 (that is 1)
            
            if l1 or l2 or carry:
                l3.next = ListNode(0) #Keep space for next val to add
                l3 = l3.next
                
        return head
            
            