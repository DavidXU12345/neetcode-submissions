class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {'[': ']', '(': ')', '{': '}'}
        closes = {']', ')', '}'}
        for ch in s:
            print(stack)
            if stack and ch in closes:
                if open_to_close[stack.pop()] != ch:
                    return False
            stack.append(ch)
        return True