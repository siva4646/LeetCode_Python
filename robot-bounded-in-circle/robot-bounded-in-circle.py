class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1,0), (0,-1), (1,0)]
        x, y = 0, 0
        d = 0
        for i in instructions:
            if i == "L":
                d = (d + 1) % 4
            elif i == "R":
                d = (d + 3) % 4
            else:
                x += dirs[d][0]
                y += dirs[d][1]
        if d != 0 or (x == 0 and y == 0):
            return True
        return False
        
        