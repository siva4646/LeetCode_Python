# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # Instead of sort we can maintain max and min then iterate through it.
        
        result = []
        
        if root == None:
            return result
        
        queue = deque()
        queue_col = deque()
        hashmap = collections.defaultdict(list)
        mini = 0
        maxi = 0
        queue.append(root)
        queue_col.append(0)
        
        while queue: # Size variable
            curr = queue.popleft()
            col = queue_col.popleft()
            
            if col not in hashmap:
                hashmap[col] = []
    
            hashmap[col].append(curr.val)
            #print(hashmap)
            # left child
            if curr.left != None:
                queue.append(curr.left)
                queue_col.append(col - 1)
                mini = min(mini, col-1)
                #print(mini)
            # right child
            if curr.right != None:
                queue.append(curr.right)
                queue_col.append(col + 1)
                maxi = max(maxi, col+1)
                #print(maxi)
        for val in range(mini, maxi+1):
            #print("value-->", val)
            result.append(hashmap[val])
        
        #print(result)
        return result
        