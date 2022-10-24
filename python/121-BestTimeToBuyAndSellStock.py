from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(prices)):
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return res

solution = Solution()

print(solution.maxProfit([7, 1, 5, 3, 6, 4])) # Expected output: 5
print(solution.maxProfit([7, 6, 4, 3, 1])) # Expected output: 0
print(solution.maxProfit([1, 2])) # Expected output: 1