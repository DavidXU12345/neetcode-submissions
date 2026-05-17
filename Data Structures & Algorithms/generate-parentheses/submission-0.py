class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count, close_count, res, current):
            # print(current)
            if len(current) == 2 * n:
                res.append(current)
                return
            if open_count < n:
                backtrack(open_count + 1, close_count, res, current + '(')
            if open_count > close_count:
                backtrack(open_count, close_count + 1, res, current + ')')
        res = []
        backtrack(0, 0, res, '')
        return res
