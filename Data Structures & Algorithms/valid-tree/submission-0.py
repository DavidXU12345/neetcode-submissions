class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for child in adj[node]:
                if child == par:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n