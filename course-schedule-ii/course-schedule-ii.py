class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        dic = collections.defaultdict(list)
        queue = deque()
        result = []
        
        for course, prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course] += 1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        # no independent node initally cannot take any course in initally phase        
                
        while queue:
            current_course = queue.popleft()
            result.append(current_course)
          
            edge = dic[current_course]
            
            for nextcourse in edge:
                indegree[nextcourse] -= 1
                
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
                    
        if len(result) == numCourses:
            return result
        else:
            return []
        