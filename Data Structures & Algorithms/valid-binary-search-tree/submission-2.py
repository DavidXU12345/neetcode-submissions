# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(node, max_val, min_val):
            if not node:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            
            return is_valid_bst(node.left, node.val, min_val) and is_valid_bst(node.right, max_val, node.val)
        
        return is_valid_bst(root, float('inf'), float('-inf'))
        
