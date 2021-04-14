# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        # Mistake did is need to focus on Two pointer you cannot take head and do head.next.next
        # KEY Is 
        # Maintaing prev and head back to back
        
        prev = dummyNode
        while head != None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummyNode.next
        
        
        
        
        
        # while head != None:
        #     if head.val == val:
        #         head.next = head.next.next 
        #     else:
        #         head = head.next
        # return dummyNode.next