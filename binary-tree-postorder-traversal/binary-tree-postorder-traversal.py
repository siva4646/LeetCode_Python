# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            root = stack.pop()
            result.append(root.val)
            
            if root.left != None:
                stack.append(root.left)
            
            if root.right != None:
                stack.append(root.right)
                
        return result[::-1]
        