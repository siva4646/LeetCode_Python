# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        slow = fast = head
        for _ in range(k - 1):
            fast = fast.next
        first_node_swap = fast
        fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        slow.val, first_node_swap.val = first_node_swap.val, slow.val
        return head
        