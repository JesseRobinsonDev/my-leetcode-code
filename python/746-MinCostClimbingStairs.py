from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Neetcode implementation
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

        # My implementation, same thing, just uses two variables instead of just the cost array
        oneStep, twoStep = cost[-1], 0
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            temp = oneStep
            oneStep = min(oneStep, twoStep) + cost[i]
            twoStep = temp

        return min(oneStep, twoStep)

solution = Solution()

print(solution.minCostClimbingStairs([10, 15, 20])) # Expected output 15
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # Expected output 6