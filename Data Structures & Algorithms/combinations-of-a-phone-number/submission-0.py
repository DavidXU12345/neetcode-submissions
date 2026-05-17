class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        def backtrack(i, comb):
            if i == len(digits):
                res.append("".join(comb))
                return
            letters = digit_to_letters[digits[i]]
            for l in letters:
                comb.append(l)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(0, [])
        return res
            