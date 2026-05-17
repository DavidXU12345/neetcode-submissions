class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            curr_res = []
            for r in res:
                curr_res.append(r + [num])
            res.extend(curr_res)
            
        return res