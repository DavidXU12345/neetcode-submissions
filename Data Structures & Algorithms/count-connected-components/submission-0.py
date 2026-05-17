class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited = [False] * n
        # print(graph)
        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True
            for nei in graph[node]:
                dfs(nei)
        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res