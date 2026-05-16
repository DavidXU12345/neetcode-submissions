class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * (len(nums) + 1)
        right_products = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            left_products[i] = left_products[i - 1] * nums[i]
        
        for i in range(len(nums) - 1, 0, -1):
            right_products[i] = right_products[i + 1] * nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(left_products[i - 1] * right_products[i + 1])
        return res