# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root == None:
            return []
        queue = deque()
        queue.append(root)
        result = []
        temp = []
        temp.append(root.val)
        flag = True
        
        while queue:
            if flag:
                result.append(list(temp))
            else:
                result.append(reversed(list(temp)))
            flag = not flag # We have to neget not direct false
            
            for i in range(len(queue)):
                node = queue.popleft()
                temp.pop(0)
                
                if node.left != None:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right != None:
                    queue.append(node.right)
                    temp.append(node.right.val)
                    
        return result
        
        