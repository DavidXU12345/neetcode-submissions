from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # instead of choosing the first balloon to burst, choose the last balloon to burst in a subarray.
        # so that two subarrays are not connected and we can consider them independently
        nums = [1] + nums + [1]

        @cache
        def dfs(left, right):
            if left > right:
                return 0
            
            res = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                res = max(res, coins)
            return res

        return dfs(1, len(nums) - 2)
