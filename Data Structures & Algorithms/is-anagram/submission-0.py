class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sort()
        return s == t