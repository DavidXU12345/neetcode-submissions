class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            if ch in close_to_open:
                if stack and stack.pop() == close_to_open[ch]:
                    continue
                return False
            else:
                stack.append(ch)
        return len(stack) == 0