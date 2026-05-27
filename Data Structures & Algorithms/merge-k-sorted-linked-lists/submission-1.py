# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode(0)
        curr = dummy
        min_heap = []

        for lst in lists:
            if lst is not None:
                # the first node of all linked lists are pushed into the min heap
                heapq.heappush(min_heap, NodeWrapper(lst))

        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                # proceed to next node
                heapq.heappush(min_heap, NodeWrapper(node_wrapper.node.next))
        
        return dummy.next
        

