from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        most = 0
        while l < r:
            water = (r - l) * min(height[l], height[r])
            most = max(most, water)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return most

solution = Solution()

print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # Expected output: 49
print(solution.maxArea([1, 8, 1, 90, 1, 1, 1, 91, 1, 7])) # Expected output: 360
print(solution.maxArea([1, 1])) # Expected output: 1