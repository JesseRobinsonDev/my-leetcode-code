from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # O(logn * logm)
        lList, rList = 0, len(matrix) - 1,
        while lList <= rList:
            mList = (lList + rList) // 2
            if target > matrix[mList][-1]:
                lList = mList + 1
            elif target < matrix[mList][0]:
                rList = mList - 1
            else:
                break

        if lList > rList:
            return False
        
        row = matrix[(lList + rList) // 2]
        l, r = 0, len(row) - 1
        
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1

        return False

        # O(m+n)
        for i, l in enumerate(matrix):
            if l[0] > target or l[-1] < target:
                continue
            for n in l:
                if n == target:
                    return True
        
        return False

solution = Solution()

print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)) # Expected output: true
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)) # Expected output: false
print(solution.searchMatrix([[1]], 0)) # Expected output: false
print(solution.searchMatrix([[1], [3]], 1)) # Expected output: true
print(solution.searchMatrix([[1, 3, 5]], 1)) # Expected output: true
print(solution.searchMatrix([[1, 3, 5]], 2)) # Expected output: false