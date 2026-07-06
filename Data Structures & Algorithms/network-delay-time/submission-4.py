class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford Algorithm
        dist = [float('inf')] * n
        dist[k - 1] = 0

        updated = True
        while updated:
            updated = False
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
                    updated = True
        
        max_dist = max(dist)
        return max_dist if max_dist < float('inf') else -1
            
            