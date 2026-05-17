from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        res = []
        for i, num in enumerate(numbers):
            if num > 0:
                break

            if i > 0 and num == numbers[i - 1]:
                continue
    
            l, r = i + 1, len(numbers) - 1
            while l < r:
                three_sum = numbers[l] + numbers[r] + num
                if three_sum == 0:
                    res.append([num, numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while numbers[l] == numbers[l - 1]:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res

