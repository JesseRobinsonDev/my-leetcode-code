from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        changes = 0

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changes == 1:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changes += 1

        return True

solution = Solution()

print(solution.checkPossibility([4, 2, 3])) # Expected output: true
print(solution.checkPossibility([4, 2, 1])) # Expected output: false
print(solution.checkPossibility([3, 4, 2, 3])) # Expected output: false
print(solution.checkPossibility([5, 7, 1, 8])) # Expected output: true
print(solution.checkPossibility([1, 4, 1, 2])) # Expected output: true