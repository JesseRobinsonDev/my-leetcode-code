class Solution:
    def climbStairs(self, n: int) -> int:
        oneStep, twoStep = 1, 1

        for i in range(n - 1):
            temp = oneStep
            oneStep = oneStep + twoStep
            twoStep = temp
        
        return oneStep

solution = Solution()

print(solution.climbStairs(2)) # Expected output: 2
print(solution.climbStairs(3)) # Expected output: 3
print(solution.climbStairs(5)) # Expected output: 8