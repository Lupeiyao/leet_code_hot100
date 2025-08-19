from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(-1)
        dummy.next = head
        while cur.next and cur.next.next:
            next = cur.next
            cur.next = next.next
            next.next = next.next.next
            cur.next.next = next
            cur = cur.next.next
        return dummy.next
