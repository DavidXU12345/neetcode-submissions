class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()  # (-cnt, time)
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = -heapq.heappop(maxHeap) - 1
                if cnt:
                    q.append((-cnt, time + n))
            else:
                time = q[0][1]
    
            if q and q[0][1] == time:
                cnt = -q.popleft()[0]
                heapq.heappush(maxHeap, -cnt)
        return time
