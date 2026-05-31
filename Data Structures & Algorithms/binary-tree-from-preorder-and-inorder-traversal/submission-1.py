# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right
        inorder_indices = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0
        def dfs(left, right):
            nonlocal preorder_idx
            if left > right:
                return
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            mid = inorder_indices[root.val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, len(inorder) - 1)