class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visited = set()
        min_heap = [(0, 0)]
        while len(visited) < len(points):
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for dist, nei in adj[point]:
                heapq.heappush(min_heap, (dist, nei))
        
        return res