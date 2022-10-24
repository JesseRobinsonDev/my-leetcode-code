from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

solution = Solution()

print(solution.productExceptSelf([1, 2, 3, 4])) # Expected output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0,- 3, 3])) # Expected output: [0, 0, 9, 0, 0]