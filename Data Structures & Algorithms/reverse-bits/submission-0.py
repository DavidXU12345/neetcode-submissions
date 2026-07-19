class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res = res | (1 << (31 - i))
        # print(f"{res:b}")
        return res
            