class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc

                    # only push cells whose heights is bigger than the current cell to the queue
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and not ocean[new_row][new_col] and heights[r][c] <= heights[new_row][new_col]):
                        q.append((new_row, new_col))
        
        pacific = []
        atlantic = []

        # all cells at the boundary can go to either pacific or atlantic
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        # get the intersection of [row, col] which can go to both pac and atl
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res