class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        res = 0

        for p in prices:
            minPrice = min(p, minPrice)
            res = max(res, p - minPrice)
        return res