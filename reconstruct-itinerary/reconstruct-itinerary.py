class Solution(object):
    def findItinerary(self, tickets):
        self.adjList = collections.defaultdict(list)
        self.result = []    
        tickets.sort(key = lambda x:x[1])
        
        for start, end in tickets:
            if start not in self.adjList:
                self.adjList[start] = [end]
            else:
                self.adjList[start].append(end)
        self.dfs("JFK")
        return self.result[::-1]
    
    def dfs(self, s):
        while s in self.adjList and len(self.adjList[s]) > 0:
            value = self.adjList[s][0]
            self.adjList[s].pop(0)
            self.dfs(value)
            
        self.result.append(s)

        
        
        