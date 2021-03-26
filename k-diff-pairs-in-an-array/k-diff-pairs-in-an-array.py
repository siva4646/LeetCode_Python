class Solution(object):
    def findPairs(self, nums, k):
        count = Counter(nums)
        c_count = 0
        
        for key, value in count.items():
            if k == 0:
                if value > 1:
                    c_count += 1
            else:
                total = key + k
                if total in count:
                    c_count += 1
        return c_count 
                    
                
        