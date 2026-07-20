class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while l <= r and top <= bottom:
            for i in range(l, r + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][r])
            r -= 1
            if not (l <= r and top <= bottom):
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res