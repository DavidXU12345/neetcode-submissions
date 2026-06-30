class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        res = nums[0]
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, prefix, suffix)
        
        return res
