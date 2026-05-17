class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(current_res, idx):
            if idx == len(s):
                if self.isPalindrome(current_res):
                    res.append(current_res.copy())
                return
            # start a new str
            backtrack(current_res + [s[idx]], idx + 1)

            if current_res:
                last_str = current_res.pop()
                current_res.append(last_str + s[idx])
                backtrack(current_res, idx + 1)
                last_str = current_res.pop()
                last_str = last_str[:len(last_str) - 1]
                current_res.append(last_str)

        backtrack([], 0)
        return res
    
    def isPalindrome(self, current_res):
        for s in current_res:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        return True