class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        # O(n * logk)
        num_to_counts = Counter(nums)
        for num, count in num_to_counts.items():
            heapq.heappush(min_heap, [count, num])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [elem[1] for elem in min_heap]


