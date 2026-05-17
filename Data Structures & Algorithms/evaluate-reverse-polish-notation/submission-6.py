class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for t in tokens:
            if t in operators:
                a = stack.pop()
                b = stack.pop()
                result = 0
                if t == '+':
                    result = a + b
                elif t == '-':
                    result = b - a
                elif t == '*':
                    result = a * b
                else:
                    result = int(float(b) / a)
                stack.append(result)
            else:
                stack.append(int(t))
        return stack[-1]