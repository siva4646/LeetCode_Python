# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        return self.helper(root, sum)
    
    def helper(self, root, sumpath):
        if root == None:
            return False
        
        if not root.left and not root.right:
            if sumpath - root.val == 0:
                return True
            return False
        
        return self.helper(root.left, sumpath - root.val) or self.helper(root.right, sumpath - root.val)
        
        
        
            
        