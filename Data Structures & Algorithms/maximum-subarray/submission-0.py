class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currentSum = 0
        for num in nums:
            if currentSum < 0:
                currentSum = num
            else:
                currentSum += num
            res = max(res, currentSum)
        return res