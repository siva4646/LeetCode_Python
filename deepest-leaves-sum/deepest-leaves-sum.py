# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        
        while queue:
            deepTotal = 0
            queue_len = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                deepTotal += curr.val
                
                if curr.left != None:
                    queue.append(curr.left)
                    
                if curr.right != None:
                    queue.append(curr.right)
                    
        return deepTotal
                
            
        
        