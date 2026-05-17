class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            time = 0
            for p in piles:
                time += p // speed
                if p % speed > 0:
                    time += 1
            return time <= h
        
        left = 1
        right = (max(piles) // h + 1) * len(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not canFinish(mid):
                left = mid + 1
            else:
                right = mid
        return right
        