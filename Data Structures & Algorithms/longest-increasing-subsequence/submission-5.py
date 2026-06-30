class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, prev):
            if i == len(nums):
                return 0
            res = dfs(i + 1, prev)  # skip nums[i]
            if prev == -1 or nums[i] > nums[prev]:
                res = max(res, 1 + dfs(i + 1, i))  # take nums[i]
            return res

        return dfs(0, -1)