class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_to_course = defaultdict(set)
        indegrees = [0] * numCourses
        for course, pre in prerequisites:
            pre_to_course[pre].add(course)
            indegrees[course] += 1
        q = deque()
        count = 0
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            count += 1
            for nei in pre_to_course[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return count == numCourses
        
