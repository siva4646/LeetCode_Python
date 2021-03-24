class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        result = self.check(A, B, A[0])
        if result != -1:
            return result
        return self.check(A, B, B[0])
    
    def check(self, A, B, value):
        aRot = 0
        bRot = 0
        
        for i in range(len(A)):
            if A[i] != value and B[i] != value:
                return -1
            elif A[i] != value:
                aRot += 1
            elif B[i] != value:
                bRot += 1
        return min(aRot, bRot)
        