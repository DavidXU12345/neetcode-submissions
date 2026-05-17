class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed_pairs = []
        for i in range(len(position)):
            pos_speed_pairs.append((position[i], speed[i]))
        pos_speed_pairs.sort(reverse=True)
        
        for (p, s) in pos_speed_pairs:
            if stack and (target - p) / s <= (target - stack[-1][0]) / stack[-1][1]:
                continue
            stack.append((p, s))
        return len(stack)