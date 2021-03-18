class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        dic = collections.defaultdict(list)
        queue = deque()
        course_count = 0
        
        for course, prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course] += 1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        # no independent node initally cannot take any course in initally phase        
        # if not queue:
        #     return False
                
        while queue:
            current_course = queue.popleft()
            course_count += 1
          
            edge = dic[current_course]
            
            for nextcourse in edge:
                indegree[nextcourse] -= 1
                
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
                    
        return course_count == numCourses
       
        
            
        