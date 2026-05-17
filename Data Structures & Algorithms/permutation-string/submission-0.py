class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        l = 0
        for r in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            # print(s1_count, s2_count)
            s2_count[s2[l]] -= 1
            s2_count[s2[r]] += 1
            l += 1

        return False
