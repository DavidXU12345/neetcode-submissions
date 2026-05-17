from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i, num in enumerate(nums):
            heappush(max_heap, (-num, i))
            if len(max_heap) < k:
                continue
            while max_heap[0][1] < i - k + 1:
                heappop(max_heap)
            # print(i, max_heap)
            res.append(-max_heap[0][0])
        return res
            


            