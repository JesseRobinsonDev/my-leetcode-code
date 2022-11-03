class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l, r = 0, 0, 0
        chars = set()

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb")) # Expected output: 3
print(solution.lengthOfLongestSubstring("bbbbb")) # Expected output: 1
print(solution.lengthOfLongestSubstring("pwwkew")) # Expected output: 3