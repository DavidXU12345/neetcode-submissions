class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = closeCount = 0
        starCount = 0
        for ch in s:
            if ch == '(':
                openCount += 1
            elif ch == ')':
                closeCount += 1
                if closeCount + starCount < openCount :
                    return False
            else:
                starCount += 1
        
        return starCount >= abs(openCount - closeCount)