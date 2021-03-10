# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        flag = False
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                flag = True
                break
        
        # if no cycle then return None
        if not flag:
            return None
        
        fast = head
        while slow !=fast:
            slow = slow.next
            fast = fast.next
        return fast
           
            
        