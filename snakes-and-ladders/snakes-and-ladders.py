from collections import deque
# Need to work on this!

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board:
            return 0
        N = len(board)
        r = N-1
        c = 0
        boardArray = [-1] * (N*N)
        even = 0
        index = 0
        while index < N*N:
            if board[r][c] == -1:
                boardArray[index] = -1
            else:
                boardArray[index] = board[r][c] - 1
            if even % 2 == 0:
                c += 1
            else:
                c -= 1
            if c >= N:
                even += 1
                r -= 1
                c -= 1
            elif c < 0:
                even += 1
                r -= 1
                c += 1
            index += 1
        minMoves = 0
        q = deque()
        q.append(0)
        boardArray[0] = -2
        finalIndex = len(boardArray)-1
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr == len(boardArray)-1:
                    return minMoves
                for j in range(1, 7):
                    value = curr+j
                    if value <= len(boardArray)-1 and boardArray[value] != -2:
                        if boardArray[value] == -1:
                            q.append(value)
                        else:
                            q.append(boardArray[value])
                        boardArray[value] = -2
            minMoves += 1
        return -1
        