class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        
        min_nums = []
        stack = []
        
        min_nums.append(nums[0])
        
        for i in range(1, len(nums)):
            min_nums.append(min(nums[:i])) # add min to the minlist
            
        for i in range(len(nums)-1, -1, -1):
            # 4
            if( nums[i] > min_nums[i] ):
                # 5
                while( stack and stack[-1] <= min_nums[i] ):
                    stack.pop()
                # 6
                if(stack and min_nums[i] < stack[-1] < nums[i] ):
                    return True
                # 4
                stack.append(nums[i])
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
        