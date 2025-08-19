from typing import Optional
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size_a, size_b = 0, 0
        cur = headA
        while cur is not None:
            size_a += 1
            cur = cur.next
        cur = headB
        while cur is not None:
            size_b += 1
            cur = cur.next
        short_list, long_list = headA, headB if size_a <= size_b else headB, headA
        for i in range(abs(size_a - size_b)):
            long_list = long_list.next
        while short_list is not long_list:
            short_list = short_list.next
            long_list = long_list.next
        return short_list
    
print(math.)