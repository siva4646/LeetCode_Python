class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        result = []
        queue = deque()
        dic = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course] += 1
        print(dic)
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            current_course = queue.popleft()
            result.append(current_course)
            
            edge = dic[current_course]
            
            for newcourse in edge:
                indegree[newcourse] -= 1
                
                if indegree[newcourse] == 0:
                    queue.append(newcourse)
                    
        
        if len(result) == numCourses:
            return result
        else:
            return []