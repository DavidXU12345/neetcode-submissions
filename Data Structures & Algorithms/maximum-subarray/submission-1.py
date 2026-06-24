class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        res = float('-inf')

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            res = max(res, current_sum)
        return res