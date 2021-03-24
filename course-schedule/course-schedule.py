class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        count_course = 0
        queue = deque()
        dic = collections.defaultdict(list)
        
        for prereq, course in prerequisites:
            dic[prereq].append(course)
            indegree[course] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        # if not queue:
        #     return False
        while queue:
            curr_course = queue.popleft()
            count_course += 1
            edge = dic[curr_course]
            
            for newCourse in edge:
                indegree[newCourse] -= 1
                
                if indegree[newCourse] == 0:
                    queue.append(newCourse)

        return count_course == numCourses
       
        
            
        