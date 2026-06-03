class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        def backtrack(current_res):
            idx = len(current_res)
            if idx == len(digits):
                res.append(''.join(current_res))
                return
            
            for letter in digit_to_letters[digits[idx]]:
                current_res.append(letter)
                backtrack(current_res)
                current_res.pop()
        
        backtrack([])
        return res