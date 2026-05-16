class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_idx = dict()
        for idx, num in enumerate(numbers):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement] + 1, idx + 1]
            num_to_idx[num] = idx
        return []