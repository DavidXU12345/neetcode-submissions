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
                # dedeuplicate
                if i > current_idx and candidates[i] == candidates[i - 1]:
                    continue

                # reduce space complexity to avoid copying in each frame on the stack (i.e. current_res + [candidates[i]] is a copy)
                current_res.append(candidates[i])
                backtrack(total + candidates[i], current_res, i + 1)
                current_res.pop()
        
        backtrack(0, [], 0)
        return res
            