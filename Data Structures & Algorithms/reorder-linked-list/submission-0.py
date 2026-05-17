# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break the linked list to 2 parts and reverse the second part
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # begin of second list
        second = slow.next
        slow.next = None
        # reverse the second half of the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
        first, second = head, prev

        # second half can be shorter than first half
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        