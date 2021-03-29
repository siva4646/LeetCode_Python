class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = {i: 0 for i in range(1, n + 1)}
        queue = deque()
        visited_count = 0 
        step = 0
        dic = collections.defaultdict(set)
        
        for course, prereq in relations:
            dic[course].add(prereq)
            indegree[prereq] += 1
        #print(indegree, dic)
            
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            for i in range(len(queue)):
                curr_course = queue.popleft()
                visited_count += 1

                edge = dic[curr_course]

                for newcourse in edge:
                    indegree[newcourse] -= 1

                    if indegree[newcourse] == 0:
                        queue.append(newcourse)
            step += 1
        
        #print(visited_count)
        if visited_count == n:
            return step
        return -1
        