class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n

        while left < right:
            mid = left + (right - left) // 2
            mid_row = mid // n
            mid_col = mid % n
            if matrix[mid_row][mid_col] > target:
                right = mid + 1
            elif matrix[mid_row][mid_col] < target:
                left = mid - 1
            else:
                return True
        return False