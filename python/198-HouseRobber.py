from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

solution = Solution()

print(solution.rob([1, 2, 3, 1])) # Expected output: 4
print(solution.rob([2, 7, 9, 3, 1])) # Expected output: 12
print(solution.rob([2, 3, 2])) # Expected output: 4