from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2

        @lru_cache(None)
        def dfs(idx, current_sum):
            if current_sum == target:
                return True
            
            if current_sum > target or idx >= len(nums):
                return False

            return dfs(idx + 1, current_sum) or dfs(idx + 1, current_sum + nums[idx])
        
        return dfs(0, 0)
