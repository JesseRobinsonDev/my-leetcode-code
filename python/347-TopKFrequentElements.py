from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        valuedList = [[] for i in range(len(nums) + 1)]

        for x in nums:
            numCount[x] = 1 + numCount.get(x, 0)
        
        for n, v in numCount.items():
            valuedList[v].append(n)

        res = []
        for i in range(len(valuedList) - 1, 0, -1):
            for n in valuedList[i]:
                res.append(n)
                if len(res) == k:
                    return res

solution = Solution()

print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) # Expected output: [1, 2]
print(solution.topKFrequent([1], 1)) # Expected output: [1]