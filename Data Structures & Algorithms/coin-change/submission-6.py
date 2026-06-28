class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque([0])
        count = 0
        seen = [False] * (amount + 1)
        seen[0] = True
        while q:
            count += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for c in coins:
                    new_cur = c + cur
                    if new_cur == amount:
                        return count
                    if new_cur > amount or seen[new_cur]:
                        continue
                    seen[new_cur] = True
                    q.append(new_cur)

        return -1
