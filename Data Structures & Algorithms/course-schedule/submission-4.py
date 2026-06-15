class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = defaultdict(list)
        for a, b in prerequisites:
            neighbors[b].append(a)
            indegree[a] += 1
        

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        finished = 0

        while q:
            crs = q.popleft()
            finished += 1

            for nei in neighbors[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finished == numCourses
