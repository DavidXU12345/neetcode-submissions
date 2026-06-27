from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def min_cost(i):
            if i == 0:
                return 0
            if i == 1:
                return 0
            return min(min_cost(i - 1) + cost[i - 1], min_cost(i - 2) + cost[i - 2])
        return min_cost(len(cost))