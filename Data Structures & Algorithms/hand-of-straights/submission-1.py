class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)

        for num in hand:
            start = num
            while counter[start - 1]:
                start -= 1
            
            while start <= num:
                while counter[start]:
                    for i in range(start, start + groupSize):
                        if not counter[i]:
                            return False
                        counter[i] -= 1
                start += 1
        return True
                