from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9)) # Expected output: [1, 2]
print(solution.twoSum([2, 3, 4], 6)) # Expected output: [1, 3]
print(solution.twoSum([-1, 0], -1)) # Expected output: [1, 2]
print(solution.twoSum([-3, 3, 4, 90], 0)) # Expected output: [1, 2]