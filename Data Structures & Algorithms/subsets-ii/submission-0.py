class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(idx, current_res):
            res.append(current_res[::])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                current_res.append(nums[i])
                backtrack(i + 1, current_res)
                current_res.pop()
        
        backtrack(0, [])
        return res