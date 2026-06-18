class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)  # all prerequisites of a course are taken before it
        
        visiting = set()
        visited = set()
        res = []
        def dfs(current_course):
            if current_course in visiting:
                return False
            if current_course in visited:
                return True
            
            visiting.add(current_course)
            for nei in graph[current_course]:
                if not dfs(nei):
                    return False
            
            visiting.remove(current_course)
            visited.add(current_course)
            res.append(current_course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return res
