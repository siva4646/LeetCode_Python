class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if not prerequisites or len(prerequisites) == 0:
        #     return []
        
        indegree = [0] * numCourses
        result = []
        queue = deque()
        dic = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course] += 1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr_course = queue.popleft()
            result.append(curr_course)
            
            edge = dic[curr_course]
            
            for newcourse in edge:
                indegree[newcourse] -= 1
                
                if indegree[newcourse] == 0:
                    queue.append(newcourse)
                    
        if len(result) == numCourses:
            return result
        else:
            return []