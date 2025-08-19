from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_tail = dummy = ListNode(-1)
        dummy.next = cur = head
        cnt = 0
        while cur and cnt <= k:
            cur = cur.next
            cnt += 1
            if cnt == k:
                cnt = 0
                new_head, new_tail = self.reverse(pre_tail.next, k)
                pre_tail.next = new_head
                new_tail.next = cur
                pre_tail = new_tail
        return dummy.next



    def reverse(self, head: ListNode, k):
        pre = None
        cur = head 
        for i in range(k):
            tmp = cur
            cur = cur.next
            tmp.next = pre
            pre = tmp
        return pre, head
            

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
Solution().reverseKGroup(l1, 2)