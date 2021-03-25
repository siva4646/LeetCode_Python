class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        dic = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                dic[key].append(word)
        
        queue = deque()
        queue.append(beginWord)
        level = 1
        visited = set()
        
        while queue:
            for k in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    key = word[:i] + "*" + word[i+1:]
                    for neighbor in dic[key]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            level += 1
        return 0
                    
            
        