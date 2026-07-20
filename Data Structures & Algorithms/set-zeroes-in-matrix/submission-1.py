class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # space optimized
        # use first row to record which column is zeroed
        # use first col to record which row is zeroed
        # (0, 0) needs to be handled more carefully since it is intersection
        m = len(matrix)
        n = len(matrix[0])
        row_zero = False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0

        if row_zero:
            for j in range(n):
                matrix[0][j] = 0