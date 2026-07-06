class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        node_to_time = [float('inf') for i in range(1, n + 1)]
        def dfs(node, time):
            if time >= node_to_time[node - 1]:
                return
            node_to_time[node - 1] = time
            for nei, weight in adj[node]:
                dfs(nei, time + weight)

        dfs(k, 0)
        res = max(node_to_time)
        return -1 if res == float('inf') else res
