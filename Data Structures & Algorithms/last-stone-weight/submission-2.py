class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x - y)
        
        return -max_heap[0] if max_heap else 0

