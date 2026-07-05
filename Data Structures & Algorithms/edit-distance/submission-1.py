from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dist = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dist[0][0] = 0
        dq = deque([(0, 0)])

        while dq:
            i, j = dq.popleft()

            if i == m and j == n:
                return dist[m][n]

            # match — cost 0, push to front
            if i < m and j < n and word1[i] == word2[j]:
                if dist[i][j] < dist[i + 1][j + 1]:
                    dist[i + 1][j + 1] = dist[i][j]
                    dq.appendleft((i + 1, j + 1))

            # replace — cost 1
            if i < m and j < n:
                if dist[i][j] + 1 < dist[i + 1][j + 1]:
                    dist[i + 1][j + 1] = dist[i][j] + 1
                    dq.append((i + 1, j + 1))

            # delete — cost 1
            if i < m:
                if dist[i][j] + 1 < dist[i + 1][j]:
                    dist[i + 1][j] = dist[i][j] + 1
                    dq.append((i + 1, j))

            # insert — cost 1
            if j < n:
                if dist[i][j] + 1 < dist[i][j + 1]:
                    dist[i][j + 1] = dist[i][j] + 1
                    dq.append((i, j + 1))

        return dist[m][n]