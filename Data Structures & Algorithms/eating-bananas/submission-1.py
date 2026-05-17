class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time <= h
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            if not canFinish(mid):
                left = mid + 1
            else:
                right = mid
        return right
        