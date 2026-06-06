class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, [x, y]))
            elif distance < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, [x, y]))
        
        return [point for _, point in max_heap]
