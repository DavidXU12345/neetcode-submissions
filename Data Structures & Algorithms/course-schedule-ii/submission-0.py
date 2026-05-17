class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_to_course = defaultdict(set)
        indegrees = [0] * numCourses
        for course, pre in prerequisites:
            pre_to_course[pre].add(course)
            indegrees[course] += 1
        q = deque()
        res = []
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            res.append(course)
            for nei in pre_to_course[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []