class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev_t, prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append([t, i])
        
        return result

