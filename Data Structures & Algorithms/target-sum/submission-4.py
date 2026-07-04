from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache
        def dfs(i, current):
            if i >= len(nums):
                return current == target
            
            return dfs(i + 1, current + nums[i]) + dfs(i + 1, current - nums[i])
        
        return dfs(0, 0)
