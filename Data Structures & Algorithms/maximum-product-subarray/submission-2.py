class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Negative numbers flip signs. If a subarray has an even number of negatives, the full product is positive.
        If it has an odd number of negatives, removing either:
        - the prefix up to the first negative, or
        - the suffix after the last negative will give the maximum product.
        
        Zeros break subarrays completely, so products must restart after a zero.
        """
        prefix = 0
        suffix = 0
        res = nums[0]
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, prefix, suffix)
        
        return res
