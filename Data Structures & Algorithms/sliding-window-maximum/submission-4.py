class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #max value => 2 1 1
        if len(nums) < k:
            return [max(nums)]
        max_heap = []
        res = []
        left = 0
        right = k - 1
        for i in range(0, k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        while right < len(nums):
            # always clean stale state first
            while max_heap and max_heap[0][1] < left:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
            right += 1
            left += 1
            if right < len(nums):
                heapq.heappush(max_heap, (-nums[right], right))
        return res