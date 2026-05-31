class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_cnt, close_cnt, current_res):
            if open_cnt > n or close_cnt > open_cnt:
                return
            if len(current_res) == n * 2:
                res.append(''.join(current_res))
                return
            
            current_res.append('(')
            backtrack(open_cnt + 1, close_cnt, current_res)
            current_res.pop()

            current_res.append(')')
            backtrack(open_cnt, close_cnt + 1, current_res)
            current_res.pop()

        backtrack(0, 0, [])
        return res