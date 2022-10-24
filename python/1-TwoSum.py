from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}

        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in numsHash:
                return [numsHash[diff], i]

            numsHash[n] = i

solution = Solution()

print(solution.twoSum([2, 1, 5, 3], 4)) # Expected output: [1, 3]
print(solution.twoSum([2, 7, 11, 15], 9)) # Expected output: [0, 1]
print(solution.twoSum([7, 3, 9, 6, 1, 8, 2, 4], 5)) # Expected output: [1, 6]
print(solution.twoSum([3, 5, 2, 3, 4, 3], 6)) # Expected output: [0, 3]