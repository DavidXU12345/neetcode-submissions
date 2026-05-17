"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = dict()

        def dfs(root):
            if not root:
                return

            if root in old_to_new:
                return old_to_new[root]
            
            new_root = Node(val=root.val)
            old_to_new[root] = new_root
            for nei in root.neighbors:
                new_root.neighbors.append(dfs(nei))
            
            return new_root
        return dfs(node)