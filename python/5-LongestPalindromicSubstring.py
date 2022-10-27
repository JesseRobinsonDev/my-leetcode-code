class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            oddPalindrome = self.getPalindrome(s, i, i)
            evenPalindrome = self.getPalindrome(s, i, i + 1)
            if len(oddPalindrome) > len(evenPalindrome) and len(oddPalindrome) > len(res):
                res = oddPalindrome
            elif len(evenPalindrome) > len(res):
                res = evenPalindrome

        return res

    def getPalindrome(self, s: str, l: int, r: int):
        resLen = 0
        resL = 0
        resR = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resLen = r - l + 1
                resL = l
                resR = r
            l -= 1
            r += 1
        return s[resL:resR + 1]

solution = Solution()

print(solution.longestPalindrome("babad")) # Expected output "bab"
print(solution.longestPalindrome("cbbd")) # Expected output "bb"
print(solution.longestPalindrome("ccc")) # Expected output "ccc"