class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cost = float('inf')
        for p in prices:
            max_profit = max(max_profit, p - cost)
            cost = min(cost, p)
        return max_profit