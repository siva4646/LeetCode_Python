# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        self.dfs(root)
        return self.moves
    # Start from depth since DFS that is at 0 left child in ex: 1       
    def dfs(self,root):
        # base
        if root == None:
            return 0
    
        # logic
        extra = root.val - 1
        extra += self.dfs(root.left)
        extra += self.dfs(root.right)
        self.moves += abs(extra)
        return extra
        