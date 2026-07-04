from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, current_sum):
            if current_sum == amount:
                return 1
            
            if i >= len(coins) or current_sum > amount:
                return 0
        
            return dfs(i + 1, current_sum) + dfs(i, current_sum + coins[i])
        return dfs(0, 0)