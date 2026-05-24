class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0
        right = len(s1)
        while right < len(s2):
            if matches == 26:
                return True
            
            # we moved "right" to right by 1
            i = ord(s2[right]) - ord('a')
            s2_count[i] += 1
            if s1_count[i] == s2_count[i]:
                matches += 1
            elif s1_count[i] + 1 == s2_count[i]:
                # previously match, but after adding the "right" ch, it doesn't match any more
                matches -= 1
                        
            # we moved "left" to right by 1
            i = ord(s2[left]) - ord('a')
            s2_count[i] -= 1
            if s1_count[i] == s2_count[i]:
                matches += 1
            elif s1_count[i] - 1 == s2_count[i]:
                matches -= 1
            left += 1
            right += 1
        return matches == 26
                        

            