from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = 0

        @lru_cache(None)
        def dfs(current_sum, idx):
            if current_sum > amount:
                return
            nonlocal count
            if current_sum == amount:
                count += 1
                return
            
            for i in range(idx, len(coins)):
                dfs(current_sum + coins[i], i)
        
        dfs(0, 0)
        return count