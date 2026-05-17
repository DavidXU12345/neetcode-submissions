class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        If heights[i] is smaller, then any future container using index i will have a smaller width, 
        and its height is still at most heights[i]. 
        So it cannot produce a larger area than the current pair. 
        Therefore, we can safely discard the smaller height and move that pointer inward. 
        The same logic applies when heights[j] is smaller.
        """
        i = 0
        j = len(heights) - 1
        ans = 0
        while i < j:
            current_area = (j - i) * min(heights[i], heights[j])
            ans = max(ans, current_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return ans