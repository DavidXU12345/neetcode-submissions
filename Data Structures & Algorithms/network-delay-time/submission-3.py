class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        min_heap = [(0, k)]  # time, node
        # Dijkstra guarantees that the first time you pop a node, you have its shortest path. 
        # Every later pop for that node has an equal or longer distance. The visit set lets you skip those stale entries.
        visit = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in adj[n1]:
                heapq.heappush(min_heap, (w1 + w2, n2))
        return t if len(visit) == n else -1