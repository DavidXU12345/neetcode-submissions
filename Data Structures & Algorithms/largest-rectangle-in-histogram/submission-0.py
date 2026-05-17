class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair (idx, h)

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                currentArea = h * (i - idx)
                maxArea = max(currentArea, maxArea)
                start = idx
            stack.append((start, heights[i]))
        
        n = len(heights)
        while stack:
            idx, h = stack.pop()
            currentArea = h * (n - idx)
            maxArea = max(currentArea, maxArea)
        return maxArea