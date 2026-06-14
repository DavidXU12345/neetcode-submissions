class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS
        visit = set()
        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        q.append((new_row, new_col))

        return time if fresh == 0 else -1