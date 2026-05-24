class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        left = right = 0

        while right < len(nums):
            # get rid of all smaller numbers before right index
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            # window has passed the left boundary
            if q[0] < left:
                q.popleft()
            
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        return res
