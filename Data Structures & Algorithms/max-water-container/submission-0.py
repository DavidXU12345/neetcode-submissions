class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        right_longest = heights[right]
        left_longest = heights[left]
        max_area = 0
        while right > left:
            current_area = (right - left) * min(heights[right], heights[left])
            max_area = max(max_area, current_area) 
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area

