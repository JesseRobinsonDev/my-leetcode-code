from typing import List

class Solution:
    def containsDuplication(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

solution = Solution();

print(solution.containsDuplication([1, 2, 3, 1])) # Expected output: True
print(solution.containsDuplication([1, 2, 3, 4])) # Expected output: False
print(solution.containsDuplication([1, 2, 1, 3])) # Expected output: True
print(solution.containsDuplication([1, 2, 0, 3])) # Expected output: False