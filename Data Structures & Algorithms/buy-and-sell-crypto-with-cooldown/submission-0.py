from functools import lru_cache
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buy or sell or cooldown
        # We can always cooldown, but can only either buy or sell at one time
        @lru_cache(None)
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                return max(buy, cooldown)

            sell = dfs(i + 2, True) + prices[i]
            return max(sell, cooldown)

        return dfs(0, True)