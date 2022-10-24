from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for x in nums:
            if x - 1 in numSet:
                continue
            newLongest = 0
            while x + newLongest in numSet:
                newLongest += 1
            longest = max(longest, newLongest)

        return longest

solution = Solution()

print(solution.longestConsecutive([100, 4, 200, 1, 3, 2])) # Expected output: 4
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # Expected output: 9