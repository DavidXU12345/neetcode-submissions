class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # guarantee there is a valid starting point
        res = 0
        total = 0
        for i in range(len(gas) - 1):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
            
        return res