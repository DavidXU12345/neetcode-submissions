from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dfs(i - 2) + nums[i], dfs(i - 1))
        return dfs(len(nums) - 1)