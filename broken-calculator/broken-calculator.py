# Optimized Way of doing this
class Solution(object):
    def brokenCalc(self, X, Y):
        count = 0
        while Y > X:
            if Y % 2 == 0:
                Y = Y // 2
            else:
                Y += 1
            count += 1
        print(count, Y)
            
        return count + X - Y
         
        