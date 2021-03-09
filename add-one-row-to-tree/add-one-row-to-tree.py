# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d <= 0:
            return root
        if d == 1:
            return TreeNode(v, root)
        
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if depth == d - 1:
                    node.left = TreeNode(v, node.left)
                    node.right = TreeNode(v, None, node.right)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if depth == d - 1:
                break
        return root
                        