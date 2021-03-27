class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        count = 1
        
        while j < len(chars) - 1:
            if chars[j] == chars[j+1]:
                count += 1
            else:
                chars[i] = chars[j]
                i += 1
                
                if count > 1:
                    for ch in str(count):
                        chars[i] = ch
                        i += 1
                        
                count = 1
            j += 1
                
        chars[i] = chars[j]
        i += 1

        if count > 1:
            for ch in str(count):
                chars[i] = ch
                i += 1

        count = 0
        
        return i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dic = {}
        # result = []
        # for char in chars:
        #     if char not in dic:
        #         dic[char] = 1
        #     else:
        #         dic[char] += 1
        # for key, value in dic.items():
        #     result.append(key)
        #     result.append(str(value))
        # return result
        
        
        
        