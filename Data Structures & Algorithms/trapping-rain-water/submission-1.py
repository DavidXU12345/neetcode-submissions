class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        highest = 0
        for h in height:
            highest = max(h, highest)
            left.append(highest)
        
        right = [0] * len(height)
        highest = 0
        for i in reversed(range(len(height))):
            highest = max(height[i], highest)
            right[i] = highest
        
        res = 0
        for i in range(1, len(height)):
            res += min(left[i], right[i]) - height[i]
        return res
