class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num or len(num) == 0:
            return False
            
        dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        left = 0
        right = len(num) - 1
        
        while left <= right:
            if num[left] not in dic or dic[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
            
        return True