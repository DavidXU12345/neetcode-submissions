class Solution:
    def hammingWeight(self, n: int) -> int:
        # n & (n - 1) clears out the lowest bit
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count