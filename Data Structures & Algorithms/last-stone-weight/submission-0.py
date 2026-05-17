class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            x *= -1
            y *= -1
            if x != y:
                heapq.heappush(maxHeap, -abs(x - y))
        return -maxHeap[0] if maxHeap else 0
            