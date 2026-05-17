class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {'[': ']', '(': ')', '{': '}'}
        for ch in s:
            if stack and open_to_close[stack[-1]] != ch:
                return False
            stack.append(ch)
        return True