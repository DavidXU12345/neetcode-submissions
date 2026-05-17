class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {'[': ']', '(': ')', '{': '}'}
        closes = {']', ')', '}'}
        for ch in s:
            # print(stack)
            if ch in closes:
                if not stack or open_to_close[stack.pop()] != ch:
                    return False
                continue
            stack.append(ch)
        return len(stack) == 0