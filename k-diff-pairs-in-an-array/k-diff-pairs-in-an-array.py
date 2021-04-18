class Solution(object):
    def findPairs(self, nums, k):
        hashMap = {}
        count = 0
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
                
        
        for key, value in hashMap.items():
            if k == 0:
                if value > 1:
                    count += 1
            else:
                total = key + k
                if total in hashMap:
                    count += 1
                    
        return count
        