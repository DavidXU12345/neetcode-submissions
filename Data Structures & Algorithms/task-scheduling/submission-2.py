class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]  # to idleTime
            else:
                # process from max heap
                cnt = - heapq.heappop(max_heap) - 1 # decrement count by 1

                if cnt > 0:
                    q.append([-cnt, time + n])
            
            if q and q[0][1] == time:
                # idleTime == time, the task in idle queue is ready to be processed next
                heapq.heappush(max_heap, q.popleft()[0])
        return time