class Solution:
    def isHappy(self, n: int) -> bool:
        # Optimize space complexity without using a seen hash set
        slow, fast = n, self.sum_of_square(n)
        while slow != fast:
            slow = self.sum_of_square(slow)
            fast = self.sum_of_square(fast)
            fast = self.sum_of_square(fast)
        
        return fast == 1

    def sum_of_square(self, n):
        res = 0

        while n:
            digit = n % 10
            digit **= 2
            res += digit
            n //= 10
        
        return res