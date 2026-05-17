from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')

        @lru_cache(None)
        def backtrack(current_sum, num_coins):
            nonlocal res
            if current_sum > amount:
                return

            if current_sum == amount:
                res = min(res, num_coins)
                return
            
            for coin in coins:
                backtrack(current_sum + coin, num_coins + 1)
        
        backtrack(0, 0)
        return -1 if res == float('inf') else res

