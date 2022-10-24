from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 + n1)
            elif n == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif n == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 * n1)
            elif n == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(n))
        
        return stack[0]

solution = Solution()

print(solution.evalRPN(["2", "1", "+", "3", "*"])) # Expected output: 9
print(solution.evalRPN(["4", "13", "5", "/", "+"] )) # Expected output: 6
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) # Expected output: 22