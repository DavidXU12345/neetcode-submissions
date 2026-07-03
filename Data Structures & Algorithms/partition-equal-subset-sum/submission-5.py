from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        @lru_cache(None)
        def helper(i, target):
            if target == 0:
                return True
            
            if i >= len(nums) or target < 0:
                return False
            
            return helper(i + 1, target - nums[i]) or helper(i + 1, target)

        return helper(0, sum(nums) // 2)