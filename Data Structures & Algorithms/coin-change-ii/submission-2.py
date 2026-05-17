from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(current_sum, idx):
            if current_sum > amount:
                return 0
            if current_sum == amount:
                return 1
            count = 0
            for i in range(idx, len(coins)):
                count += dfs(current_sum + coins[i], i)
            return count
        
        return dfs(0, 0)