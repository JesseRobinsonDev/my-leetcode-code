from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1

solution = Solution()

print(solution.search([-1, 0, 3, 5, 9, 12], 9)) # Expected output: 4
print(solution.search([-1, 0, 3, 5, 9, 12], 2)) # Expected output: -1
print(solution.search([5], 5)) # Expected output: 0