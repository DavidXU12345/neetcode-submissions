class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(current_sum, current_res, idx):
            if current_sum == target:
                res.append(current_res)
                return
            
            if current_sum > target:
                return
            for i in range(idx, len(nums)):
                dfs(current_sum + nums[i], current_res + [nums[i]], i)
        
        dfs(0, [], 0)
        return res