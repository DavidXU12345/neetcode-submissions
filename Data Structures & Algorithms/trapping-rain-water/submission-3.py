class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * (len(height) + 1)
        right = [0] * (len(height) + 1)
        for i, h in enumerate(height):
            left[i] = max(h, left[i-1])
        
        for i in range(len(height) - 1, -1, -1):
            right[i] = max(height[i], right[i+1])
        
        area = 0
        for i, h in enumerate(height):
            area += max(0, (min(left[i], right[i]) - h))
        return area
