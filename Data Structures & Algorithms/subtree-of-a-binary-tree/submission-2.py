# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not q and not p:
                return True
            
            if (not q and p) or (not p and q) or q.val != p.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if isSameTree(root, subRoot):
            return True
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)
        