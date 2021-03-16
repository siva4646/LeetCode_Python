# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #Time and space is O(N)
        if root == None:
            return None
        
        queue = deque()
        queue.append(root)
        result = []
        temp = []
        temp.append(root.val)
        
        while queue:
            result.append(list(temp))
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                # Missed temp.pop()
                temp.pop(0)
                
                if node.left != None:
                    queue.append(node.left)
                    temp.append(node.left.val)
                    
                if node.right != None:
                    queue.append(node.right)
                    temp.append(node.right.val)
            
        return result
                    
        
            
                    
            