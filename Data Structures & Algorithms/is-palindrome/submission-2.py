class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s.lower() if char.isalnum())
        mid_point = len(clean_text) // 2
        if len(clean_text) % 2 == 1:
            i = 0
            j = len(clean_text) - 1
            while i < mid_point:
                if clean_text[i] != clean_text[j]:
                    return False
                i += 1
                j -= 1
        else:
            i = 0
            j = len(clean_text) - 1
            while i < mid_point:
                if clean_text[i] != clean_text[j]:
                    return False
                i += 1
                j -= 1
        return True

