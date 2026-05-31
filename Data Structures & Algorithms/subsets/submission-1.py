class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current_res: List[int], idx):
            if idx >= len(nums):
                res.append(current_res[:])
                return
            backtrack(current_res, idx + 1)  # not include current num
            backtrack(current_res + [nums[idx]], idx + 1)  # include current num
        backtrack([], 0)
        return res