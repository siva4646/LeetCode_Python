import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums, token = set(), ''
        
        for i, l in enumerate(word):
            if token != '' and l.isalpha():
                nums.add(int(token))
                print(nums)
                token = ''
            elif l.isnumeric():
                token += l
                
            if i == len(word) - 1 and l.isnumeric():
                nums.add(int(token))
               
                    
        return len(nums)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hashset = set()
#         each_num = ""
#         left = 0
#         right = 0
#         while left < len(word):
#             if word[left].isdigit() or word[right].isdigit():
#                 each_num += word[left]
#                 right += 1
#             hashset.add(each_num)
            
#             left += 1
#             right += 1
#         print(hashset)
        