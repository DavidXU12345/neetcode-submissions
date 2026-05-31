class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(idx, current_res):
            if idx >= len(nums):
                res.append(current_res[:])
                return
            # include nums[idx]
            current_res.append(nums[idx])
            backtrack(idx + 1, current_res)
            current_res.pop()

            # dedup
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            # exclude nums[idx]
            backtrack(idx + 1, current_res)
        
        backtrack(0, [])
        return res