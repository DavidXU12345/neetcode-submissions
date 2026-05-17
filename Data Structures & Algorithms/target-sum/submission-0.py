from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(current_sum, idx):
            if idx > len(nums):
                return 0
            if current_sum == target and idx == len(nums):
                return 1
            count = 0
            for i in range(idx, len(nums)):
                count += dfs(current_sum + nums[i], idx + 1)
                count += dfs(current_sum - nums[i], idx + 1)
            
            return count
        return dfs(0, 0)