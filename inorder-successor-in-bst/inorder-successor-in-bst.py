# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or root == None:
            return None
        
        successor = None
        while root != None:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
        