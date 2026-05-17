class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = openMax = 0
        for ch in s:
            if ch == '(':
                openMin += 1
                openMax += 1
            elif ch == ')':
                openMin -= 1
                openMax -= 1
            else:
                openMin -= 1
                openMax += 1
            if openMax < 0:
                return False
            openMin = max(openMin, 0)
        return openMin == 0
        
        return starCount >= abs(openCount - closeCount)