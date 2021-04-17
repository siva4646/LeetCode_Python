class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y= 0
        
        for move in moves:
            if move == "R":
                y += 1
            elif move == "L":
                y -= 1
            elif move == "U":
                x -= 1
            elif move == "D":
                x += 1
        return x == y == 0
            
                
        