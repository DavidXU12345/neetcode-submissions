from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(current_sum, idx):
            if idx > len(nums):
                return 0
            if idx == len(nums):
                if current_sum == target:
                    return 1
                return 0
            return dfs(current_sum + nums[idx], idx + 1) + dfs(current_sum - nums[idx], idx + 1)
        return dfs(0, 0)