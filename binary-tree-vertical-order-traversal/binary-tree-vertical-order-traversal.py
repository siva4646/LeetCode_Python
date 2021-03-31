# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        maxi = 0
        mini = 0
        result = []
        hashmap = collections.defaultdict(list)
    
        while queue:
            curr, level = queue.popleft()
            
            mini = min(mini, level)
            maxi = max(maxi, level)
            
            if level not in hashmap:
                hashmap[level] = []
            hashmap[level].append(curr.val)
            print(hashmap)
            
            if curr.left != None:
                queue.append((curr.left, level - 1))
                
            if curr.right != None:
                queue.append((curr.right, level + 1))
                
        for val in range(mini, maxi + 1):
            result.append(hashmap[val])
            
        return result
        