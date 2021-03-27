class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if (i % 3) == 0 and (i % 5) == 0:
                 result.append(str("FizzBuzz"))
            elif i % 3 == 0:
                result.append(str("Fizz"))
            elif i % 5 == 0:
                result.append(str("Buzz"))
            else:
                result.append(str(i)) # better if you add result in else
                
        return result
                
        