# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        mini = 0
        maxi = 0
        queue = deque()
        hashmap = collections.defaultdict(list)
        queue.append((root,0,0))
        
        while queue: # Size variable
            node, r, c = queue.popleft()
          
            if node != None:
                hashmap[c].append((r, node.val))
                mini = min(mini, c)
                maxi = max(maxi, c)
                
                if node.left != None:
                    queue.append((node.left, r+1, c-1))
                    
                if node.right != None:
                    queue.append((node.right, r+1, c+1))
                    
        result = []
        for col in range(mini, maxi + 1):
            result.append([val for r, val in sorted(hashmap[col])])
        return result  
            
        
        
        
        
        