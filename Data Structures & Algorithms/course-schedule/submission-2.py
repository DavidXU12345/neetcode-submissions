class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        for a, b in prerequisites:
            neighbors[b].append(a)

        visiting = set()   # current DFS path (cycle detection)
        visited = set()    # fully processed nodes (safe to skip)

        def dfs(course):
            if course in visiting:
                return False   # cycle detected
            if course in visited:
                return True    # already confirmed safe

            visiting.add(course)
            for nei in neighbors[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)  # backtrack
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

