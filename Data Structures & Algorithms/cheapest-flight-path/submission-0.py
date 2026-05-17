class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # min_heap (cost, num_stops, place)
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        
        min_heap = []
        min_heap.append((0, 0, src))
        while min_heap:
            total_cost, total_stops, place = heapq.heappop(min_heap)
            if total_stops > k + 1:
                continue
            
            if place == dst:
                return total_cost
            
            for nei, cost in graph[place]:
                heapq.heappush(min_heap, (total_cost + cost, total_stops + 1, nei))

        return -1