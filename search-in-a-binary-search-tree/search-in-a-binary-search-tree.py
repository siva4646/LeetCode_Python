# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Base case
        if root is None or val == root.val:
            return root
        
        # Logic
        if val < root.val:
            return self.searchBST(root.left, val)
        
        if val > root.val:
            return self.searchBST(root.right, val)
        
    
        