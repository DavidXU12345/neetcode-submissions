class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left, right = 0, len(nums1) - 1
        half = (len(nums1) + len(nums2)) // 2
        is_odd = (len(nums1) + len(nums2)) % 2 == 1

        while True:
            i = (left + right) // 2
            j = half - i - 2

            nums1_left = nums1[i] if i >= 0 else float('-inf')
            nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float('inf')
            nums2_left = nums2[j] if j >= 0 else float('-inf')
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if is_odd:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            if nums1_left > nums2_right:
                # index i is too big
                right = i - 1
            else:
                left = i + 1


