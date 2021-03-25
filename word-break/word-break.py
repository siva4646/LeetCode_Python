#BFS Solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        queue = deque()
        queue.append(s)
        visited = set()
        visited.add(s)
        
        while queue:
            word = queue.popleft()
            print(word)
            if word in wordDict:
                return True
            
            for i in range(1, len(word) + 1):
                if word[:i] in wordDict and word[i:] not in visited:
                    queue.append(word[i:])
                    visited.add(word[i:])
                    
        return False
                    
                
        