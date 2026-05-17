# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def height(root):
            nonlocal isBalanced

            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight) > 1:
                # if any of ndoe is not balanced, it is not balanced
                isBalanced = False
                return 0
            return 1 + max(leftHeight, rightHeight)
        
        height(root)
        return isBalanced
        
        