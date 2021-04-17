class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        minlist = []
        stack = []
        
        minlist.append(nums[0])
        
        for i in range(1, len(nums)):
            minlist.append(min(nums[:i])) # add min to the minlist
            
        for j in range(len(nums)-1, -1, -1): # length start 1 and index form 0
            if nums[j] > minlist[j]:
                while stack and stack[-1] <= minlist[j]:
                    stack.pop()
                    
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
                
        return False
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # for num in nums:
        #     while stack and stack[-1] < num:
        #         stack.pop()
        #         stack.append(num)
        #         if stack[-1] > num:
        #             stack.append(num)
        #     stack.append(num)
        # return len(stack) == 3
        