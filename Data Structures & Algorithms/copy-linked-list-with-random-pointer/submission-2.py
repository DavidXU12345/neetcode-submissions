"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = defaultdict(lambda: Node(0))
        old_to_copy[None] = None

        curr = head
        while curr:
            old_to_copy[curr].val = curr.val
            old_to_copy[curr].next = old_to_copy[curr.next]
            old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next
        return old_to_copy[head]

    