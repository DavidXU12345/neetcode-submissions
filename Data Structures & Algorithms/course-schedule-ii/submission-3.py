class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)  # take prerequisite first
            indegree[a] += 1  # course A has one more prerequisite
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        res = []
        finish = 0
        while q:
            crs = q.popleft()
            res.append(crs)
            finish += 1
            for nei in graph[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if finish != numCourses:
            return []
        return res

        
