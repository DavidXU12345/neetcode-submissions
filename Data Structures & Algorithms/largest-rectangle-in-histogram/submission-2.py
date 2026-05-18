class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Monotonic stack
        
        For every bar, we try to treat it as the shortest bar in the rectangle.
        To find how wide this rectangle can extend, we look left and right until we hit a bar shorter than the current one.
        The width between these two boundaries gives the largest rectangle where this bar is the limiting height.
        We repeat this for every bar and keep track of the maximum rectangle found.
        
        leftMost[i] — the index of the nearest bar to the left that is shorter than heights[i]
        rightMost[i] — the index of the nearest bar to the right that is shorter than heights[i]
        """
        monotonic_increasing_stack = []  # index
        # if no shorter bar is found on the left, it will use index 0 
        left_most = [-1] * len(heights)
        for i in range(len(heights)):
            while monotonic_increasing_stack and heights[monotonic_increasing_stack[-1]] >= heights[i]:
                monotonic_increasing_stack.pop()
            if monotonic_increasing_stack:
                left_most[i] = monotonic_increasing_stack[-1]
            monotonic_increasing_stack.append(i)
        
        monotonic_increasing_stack = []  # index
        # if no shorter bar is found on the right, it will use the end of heights
        right_most = [len(heights)] * len(heights)
        for i in reversed(range(len(heights))):
            while monotonic_increasing_stack and heights[monotonic_increasing_stack[-1]] >= heights[i]:
                monotonic_increasing_stack.pop()
            if monotonic_increasing_stack:
                right_most[i] = monotonic_increasing_stack[-1]
            monotonic_increasing_stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            left_idx = left_most[i] + 1
            right_idx = right_most[i] - 1
            current_area = (right_idx - left_idx + 1) * heights[i]
            max_area = max(max_area, current_area)
        
        return max_area