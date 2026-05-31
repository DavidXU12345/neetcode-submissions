class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start_idx, current_res, total):
            if total > target:
                return
            if total == target:
                res.append(current_res)
                return
            for i in range(start_idx, len(nums)):
                backtrack(i, current_res + [nums[i]], total + nums[i])
            
        backtrack(0, [], 0)
        return res
