# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in order tree traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_lst = []
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            sorted_lst.append(node.val)
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return sorted_lst[k-1]