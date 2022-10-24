from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()

solution = Solution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # Expected output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""])) # Expected output: [[""]]
print(solution.groupAnagrams(["a"])) # Expected output: [["a"]]