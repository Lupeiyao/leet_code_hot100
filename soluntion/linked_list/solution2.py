from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre = None
        while head is not None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre