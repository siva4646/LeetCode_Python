class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count_val = Counter(nums)
        print(count_val)
        count = 0
        for key, value in count_val.items():
            if k == 0:
                if value > 1:
                    count += 1
            else:
                total_val = key + k
                if total_val in count_val:
                    count += 1
                    
        return count
        