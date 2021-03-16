# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                # Queue Structure 
                # print(i, queue_len, node.val)
                # if i == queue_len - 1:
                #     result.append(node.val)
                    
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
            result.append(node.val)    # avoid O(2^n)
            
        return result
                    