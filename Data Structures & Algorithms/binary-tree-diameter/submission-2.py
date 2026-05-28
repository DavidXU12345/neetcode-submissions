# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node):
            nonlocal res
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            res = max(res, left + right)  # number of edges, not number of nodes
            return 1 + max(left, right)
        
        depth(root)
        return res