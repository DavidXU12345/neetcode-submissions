class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            else:
                digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        
        if carry > 0:
            digits.insert(0, 1)
        return digits
