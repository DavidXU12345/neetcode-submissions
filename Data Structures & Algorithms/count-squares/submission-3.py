class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts_count:
            if abs(py - y) != abs(px - x) or (py == y and px == x):
                continue
            res += (self.pts_count[(x, y)]
                    * self.pts_count.get((x, py), 0)
                    * self.pts_count.get((px, y), 0))
        return res