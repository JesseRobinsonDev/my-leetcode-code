from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

solution = Solution()

print(solution.rob([2, 3, 2])) # Expected output: 3
print(solution.rob([1, 2, 3, 1])) # Expected output: 4
print(solution.rob([1, 2, 3])) # Expected output: 3
print(solution.rob([1])) # Expected output: 1