class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        
        return n == 1
    
    def sum_of_squares(self, n):
        res = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10
        
        return res