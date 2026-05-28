# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return [True, 0]
            
            left = depth(node.left)
            right = depth(node.right)
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [is_balanced, max(left[1], right[1]) + 1]
        return depth(root)[0]