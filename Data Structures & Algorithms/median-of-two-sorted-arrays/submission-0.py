class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search the shorter list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        half = (len(nums1) + len(nums2)) // 2
        isOdd = (len(nums1) + len(nums2)) % 2 == 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1Left = nums1[i] if i >= 0 else float('-inf')
            nums1Right = nums1[i + 1] if (i + 1) < len(nums1) else float('inf')
            nums2Left = nums2[j] if j >= 0 else float('-inf')
            nums2Right = nums2[j + 1] if (j + 1) < len(nums2) else float('inf')

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if isOdd:
                    return min(nums1Right, nums2Right)
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            
            if nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1
