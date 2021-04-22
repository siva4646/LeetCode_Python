class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapMap = {}
        
        for i in range(len(wall)):
            rSum = 0
            for j in range(0, len(wall[i])-1):
                rSum = rSum + wall[i][j]
                if rSum not in gapMap:
                    gapMap[rSum] = 1
                else:
                    gapMap[rSum] += 1
        print(gapMap)
        
        maxGap = 0
        for key, value in gapMap.items():
            maxGap = max(maxGap, gapMap[key])
        return len(wall) - maxGap
        
        