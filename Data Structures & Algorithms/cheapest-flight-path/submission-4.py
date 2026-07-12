class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman–Ford is perfect here because it relaxes edges level by level, where each iteration allows one more edge in the path.
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            """
            Without tmpPrices, you'd use updated values from the current iteration to relax other edges within the same iteration, 
            effectively allowing more stops than intended.
            """
            tmp_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p
            
            prices = tmp_prices

        return -1 if prices[dst] == float('inf') else prices[dst]
