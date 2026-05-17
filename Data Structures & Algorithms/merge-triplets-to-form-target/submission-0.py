class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_x = 0
        max_y = 0
        max_z = 0
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            max_x = max(max_x, t[0])
            max_y = max(max_y, t[1])
            max_z = max(max_z, t[2])
        
        return [max_x, max_y, max_z] == target