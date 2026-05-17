from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i, num in enumerate(nums):
            heappush(max_heap, (-num, i))
            if len(max_heap) < k:
                continue
            negative_num, idx = max_heap[0]
            while idx < i - k + 1:
                negative_num, idx = heappop(max_heap)
            res.append(-negative_num)
        return res
            


            