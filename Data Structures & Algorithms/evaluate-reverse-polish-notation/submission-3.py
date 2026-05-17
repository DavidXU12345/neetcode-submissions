class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                continue
            num1 = stack.pop()
            num2 = stack.pop()
            # print(num1, t, num2)
            if t == '+':
                stack.append(num1 + num2)
            elif t == '-':
                stack.append(num2 - num1)
            elif t == '*':
                stack.append(num1 * num2)
            elif t == '/':
                stack.append(int(float(num2) / num1))

        return stack[-1]
