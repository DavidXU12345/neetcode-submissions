class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(idx, current_res, current_str):
            # print(idx, current_res, current_str)
            if idx >= len(s):
                if not current_str: # only valid if nothing left uncommitted
                    res.append(current_res[:])
                return
            new_string = current_str + s[idx]

            # Branch 1: commit new_string as a partition, reset
            if is_palindrome(new_string):
                backtrack(idx + 1, current_res + [new_string], "")

            # Branch 2: keep extending, but only if there are chars left to form a palindrome
            if idx + 1 < len(s):
                backtrack(idx + 1, current_res, new_string)
        backtrack(0, [], "")

        return res