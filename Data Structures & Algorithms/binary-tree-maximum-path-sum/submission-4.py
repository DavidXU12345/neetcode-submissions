# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftMax = max(0, dfs(node.left))   # drop if negative
            rightMax = max(0, dfs(node.right))

            res = max(res, node.val + leftMax + rightMax)  # candidate path through this node
            return node.val + max(leftMax, rightMax)       # can only extend one direction upward
        
        dfs(root)
        return res
