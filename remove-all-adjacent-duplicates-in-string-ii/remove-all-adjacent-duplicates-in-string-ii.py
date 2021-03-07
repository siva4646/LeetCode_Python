class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s or len(s) == 0 or not k:
            return s
        
        idx = 0
        while idx < len(s):
            if s[idx:idx+k] == s[idx] * k:
                # for remove or bypass k character in the s.
                s = s[:idx] + s[idx+k:]
                idx = 0
            else:
                idx += 1
        return s
            
        
          
        
# MY CODE        
#         count = 0
#         flag = True
#         result = ''
#         for i in range(len(s)-1):
#             if flag and s[i] == s[i+1] and count < k:
#                 count += 1
#                 substring = s[flag:count+1]
#                 result = s.replace(substring, '')
#             else:
#                 count = 0
#                 # flag = False
#                 #i += 1 
#         return result
      
        
        