from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, sell, do nothing

        @lru_cache(None)
        def dfs(i, holding_stock):
            if i >= len(prices):
                return 0
            do_nothing = dfs(i + 1, holding_stock)
            if holding_stock:
                # if sell, cannot buy the next day
                sell = dfs(i + 2, False) + prices[i]
                return max(do_nothing, sell)
            
            buy = dfs(i + 1, True) - prices[i]
            return max(do_nothing, buy)
        
        return dfs(0, False)

