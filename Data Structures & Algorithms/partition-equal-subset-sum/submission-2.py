class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target_sum = sum(nums) // 2
        def helper(i, current_sum):
            if current_sum == target_sum:
                return True
            
            if i == len(nums) or current_sum > target_sum:
                return False
            
            return helper(i + 1, current_sum + nums[i]) or helper(i + 1, current_sum)

        return helper(0, 0)