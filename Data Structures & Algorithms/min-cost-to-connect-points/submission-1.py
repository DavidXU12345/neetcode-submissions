class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        min_heap = [[0, 0]]
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        visit = set()
        res = 0
        while len(visit) < n:
            dist, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            
            visit.add(node)
            res += dist
            for dist, nei in adj[node]:
                heapq.heappush(min_heap, [dist, nei])
        
        return res

