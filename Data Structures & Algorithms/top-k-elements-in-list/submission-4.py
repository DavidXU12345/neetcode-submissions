class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort O(n)
        num_to_count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in num_to_count.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            res.extend(freq[i])
            if len(res) == k:
                return res