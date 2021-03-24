class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        count_province = 0
    
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                # print(i, j)
                if isConnected[i][j] == 1:
                    count_province += 1
                    self.dfs(isConnected, i)
        return count_province
    
    
    def dfs(self, isConnected, i):
        # see inside a single list
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1:
                isConnected[i][j] = "X"
                self.dfs(isConnected, j)
                
        
        