class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        INF = 2 ** 31 - 1

        def add_cell(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and grid[r][c] == INF):
                return
            visit.add((r, c))
            q.append([r, c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # it is a treasure
                    visit.add((r, c))
                    q.append([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1