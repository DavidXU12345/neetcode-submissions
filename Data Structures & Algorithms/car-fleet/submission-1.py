class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [[0, 1] -> 10 seconds, [1, 2] -> 4.5 seconds, [4, 2] -> 3 seconds => 4 seconds, [7, 1] -> 4 seconds]
        # [1 -> 3 seconds, 4 -> 3 seconds]
        position_time_pair = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            position_time_pair.append([position[i], time])
        position_time_pair.sort()
        res = len(position)
        prev_pos = -1
        prev_time = 0
        # print(position_time_pair)
        while position_time_pair:
            pos, time = position_time_pair.pop()
            if time <= prev_time:
                res -= 1
            else:
                prev_time = time
            # print(prev_time)
        return res
            
