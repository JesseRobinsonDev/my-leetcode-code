class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.turnIntoPalindrome(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
    
    def turnIntoPalindrome(self, s: str) -> str:
        ns = ""

        for c in s:
            if ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
                ns += c.lower()

        return ns

solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama")) # Expected output: True
print(solution.isPalindrome("race a car")) # Expected output: False
print(solution.isPalindrome(" ")) # Expected output: True
print(solution.isPalindrome("joisdfjisdgji")) # Expected output: False
