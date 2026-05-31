class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(total, current_res, current_idx):
            if total > target:
                return
            if total == target:
                res.append(current_res[:])

            for i in range(current_idx, len(candidates)):
                if i > current_idx and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(total + candidates[i], current_res + [candidates[i]], i + 1)
        
        backtrack(0, [], 0)
        return res
            