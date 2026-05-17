class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    fresh -= 1
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    fresh -= 1
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                if c + 1 < COLS and grid[r][c + 1] == 1:
                    fresh -= 1
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    fresh -= 1
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
            time += 1

        return time if fresh == 0 else -1         


