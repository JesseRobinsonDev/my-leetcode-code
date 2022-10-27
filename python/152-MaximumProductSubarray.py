from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            newMax, newMin = n * curMax, n * curMin
            curMax = max(newMax, newMin, n)
            curMin = min(newMax, newMin, n)
            res = max(res, curMax, curMin)
        return res

solution = Solution()

print(solution.maxProduct([2, 3, -2, 4])) # Expected output: 6
print(solution.maxProduct([2, 3, -2, 4, 8])) # Expected output: 32
print(solution.maxProduct([-2, 0, -1])) # Expected output: 0
print(solution.maxProduct([-2])) # Expected output: -2
print(solution.maxProduct([0, 2])) # Expected output: 2
print(solution.maxProduct([2, 3, 4])) # Expected output: 24