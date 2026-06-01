class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_res = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(current_res.copy())
                return
            
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current_res.append(s[i : j + 1])
                    dfs(j + 1)
                    current_res.pop()
        
        dfs(0)
        return res

        
