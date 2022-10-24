class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {")": "(", "]": "[", "}": "{"}
        stack = []

        # Pop before append
        for p in s:
            if p in pMap and len(stack) > 0 and stack[-1] == pMap[p]:
                stack.pop()
                continue
            stack.append(p)
        return not stack

        # Append before pop
        for p in s:
            if p not in pMap:
                stack.append(p)
                continue
            if not stack or stack[-1] != pMap[p]:
                return False
            stack.pop()
        return not stack

solution = Solution()

print(solution.isValid("()[]{}")) # Expected output: True
print(solution.isValid("(]")) # Expected output: False
print(solution.isValid("([([]())][])")) # Expected output: True
print(solution.isValid("()[}")) # Expected output: False