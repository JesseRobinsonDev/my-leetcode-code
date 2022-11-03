from turtle import left
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m+n), unsure if there is a faster solution
        col = 0
        row = len(matrix) - 1
        while col <= len(matrix[0]) - 1 and row >= 0:
            cell = matrix[row][col]
            if cell == target:
                return True
            elif cell > target:
                row -= 1
            elif cell < target:
                col += 1
        return False

solution = Solution()

print(solution.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)) # Expected output: true
print(solution.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)) # Expected output: false
print(solution.searchMatrix([[-5]], -5)) # Expected output: true
print(solution.searchMatrix([[-1, 3]], 3)) # Expected output: true