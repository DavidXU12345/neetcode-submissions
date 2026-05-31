class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def backtrack(current_res):
            if len(current_res) == len(nums):
                res.append(current_res[:])
                return
            
            for i in range(len(nums)):
                if pick[i]:
                    continue
                pick[i] = True
                current_res.append(nums[i])
                backtrack(current_res)
                current_res.pop()
                pick[i] = False
            
        backtrack([])
        return res
            
