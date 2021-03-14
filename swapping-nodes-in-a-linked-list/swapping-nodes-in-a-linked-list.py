# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            length += 1

        fast_move = length - k 
        
        # Slow at correct position
        while k != 1:
            slow = slow.next
            k -= 1
    
        fast = head
        while fast_move != 0:
            fast = fast.next
            fast_move -= 1
        
        slow.val , fast.val = fast.val , slow.val
        
        return head
        
        
        # print("Slow val", slow.val)
        # print("Fast val", fast.val)
 
        