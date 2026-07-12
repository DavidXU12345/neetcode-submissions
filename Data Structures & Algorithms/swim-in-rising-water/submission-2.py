class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra's Algorithm (BFS with min heap essentially)
        visit = set()
        n = len(grid)
        min_heap = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return t
            
            if (r, c) in visit:
                continue
            visit.add((r, c))
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < n and 0 <= new_c < n:
                    heapq.heappush(min_heap, [max(t, grid[new_r][new_c]), new_r, new_c])
        
        return -1