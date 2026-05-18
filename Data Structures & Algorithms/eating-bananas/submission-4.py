class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        # search space [left, right)
        while left < right:
            mid = left + (right - left) // 2
            hours = self.calculateHours(mid, piles, h)
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left

    def calculateHours(self, k, piles, h):
        result = 0
        for p in piles:
            result += p // k
            if p % k > 0:
                result += 1
        return result