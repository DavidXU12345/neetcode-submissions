class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Working heap is the heap we try to fetch and process next task while idle_q for cooldown purpose
        """
        counter = Counter(tasks)
        working_max_heap = [-cnt for cnt in counter.values()]  # count
        heapq.heapify(working_max_heap)

        idle_q = deque()  # [count, idle_time]
        time = 0
        while working_max_heap or idle_q:
            time += 1

            if working_max_heap:
                count = 1 + heapq.heappop(working_max_heap)
                if count < 0:  # still have work to do, put it in idle_q and can only be processed at or after time + n
                    idle_q.append([count, time + n])
            # else:
            #     # working heap is empty, we can only wait and process idle_q next
            #     time = idle_q[0][1]
            
            # each iteration, we check whether we can move task from idle queue to working heap
            if idle_q and idle_q[0][1] == time:
                heapq.heappush(working_max_heap, idle_q.popleft()[0])
        
        return time


