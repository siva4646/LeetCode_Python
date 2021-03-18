class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Base condition
        if not prerequisites or len(prerequisites) == 0:
            return True
        
        # Maintain indegree array since we need to know the independent node
        indegree = [0] * numCourses
        queue = deque()
        course_count = 0
        # Maintain adjacency list
        dic = collections.defaultdict(list)
        
        # fill my adjacency list key as prereq and val as course and increment my indegree of course to 1
        for course, prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course] +=1
        print(indegree)
        
        # if indegree[i] is zero once we process then add to the queue
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        if not queue:
            return False
        # process queue 
        while queue:
            current_course = queue.popleft()
            # increment since it can be taken
            course_count += 1
            
            # search in adjacency list and store it's value in edge
            edge = dic[current_course]
            
            # iterate through it and decrement indegree since it can be taken and if indegree[nextcourse] == 0 then add to the queue to process again
            for nextcourse in edge:
                indegree[nextcourse] -= 1
            
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
                    
        return course_count == numCourses
    