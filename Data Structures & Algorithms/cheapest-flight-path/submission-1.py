class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        
        min_heap = [(0, 0, src)]  # (cost, stops, node)
        best_stops = {}  # node -> fewest stops we've reached it with
        
        while min_heap:
            cost, stops, node = heapq.heappop(min_heap)
            if node == dst:
                return cost
            if stops > k:
                continue
            # Skip if we've already reached this node with fewer stops
            # We don't use visit set since it may cause
            # a cheaper but high-stop path visits a node first, then a more expensive but low-stop path gets blocked
            if node in best_stops and best_stops[node] <= stops:
                continue
            best_stops[node] = stops
            
            for nei, w in graph[node]:
                heapq.heappush(min_heap, (cost + w, stops + 1, nei))
        return -1