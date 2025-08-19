from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        plus = 0
        cur = dummy = ListNode(0)
        while l1 or l2:
            val = plus
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            plus = val // 10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next
        if plus == 1:
            cur.next = ListNode(1)       
        return dummy.next
                
                



        