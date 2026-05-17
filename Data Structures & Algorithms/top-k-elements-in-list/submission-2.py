class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq_list = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            freq_list[freq].append(num)
        
        res = []

        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
