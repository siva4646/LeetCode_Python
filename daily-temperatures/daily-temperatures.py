class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T or len(T) == 0:
            return []
        stack = []
        result = [0] * len(T)
        
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
         