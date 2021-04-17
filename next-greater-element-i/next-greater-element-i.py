class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        if not nums1 or not nums2:
            return -1
        
        stack = []
        stack.append(nums2[0])
        
        hashMap = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                hashMap[val] = nums2[i]
            stack.append(nums2[i])
            
        for key in stack:
            hashMap[key] = -1
        return [hashMap[key] for key in nums1]
            
        