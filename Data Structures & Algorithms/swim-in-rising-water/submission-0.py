class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()        
        visited.add((0, 0))
        min_heap = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1: # reached target
                return t
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if (not (0 <= new_row < N and 0 <= new_col < N)) or (new_row, new_col) in visited:
                    continue
                visited.add((new_row, new_col))
                heapq.heappush(min_heap, (max(t, grid[new_row][new_col]), new_row, new_col))
        