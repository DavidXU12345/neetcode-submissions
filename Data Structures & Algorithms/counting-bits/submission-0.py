class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n + 1):
            count = 0
            while x:
                x = x & (x - 1)
                # x = 0110
                # x - 1 = 0101
                # x & (x - 1) = 0100
                count += 1
            res.append(count)
        return res
