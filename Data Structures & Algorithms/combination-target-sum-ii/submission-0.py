class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(current_sum, current_res, idx):
            if current_sum == target:
                res.append(current_res)
                return
            if current_sum > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(current_sum + candidates[i], current_res + [candidates[i]], i + 1)
            
        dfs(0, [], 0)
        return res