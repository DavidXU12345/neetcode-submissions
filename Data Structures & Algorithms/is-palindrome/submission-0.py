class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_s = []
        clean_s = []
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            clean_s.append(s[i].lower())

        for i in reversed(range(len(clean_s))):
            reversed_s.append(clean_s[i])
        return reversed_s == clean_s
