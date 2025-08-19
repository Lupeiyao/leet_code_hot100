from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.help_merge(lists, 0, len(lists) - 1)
    
    def help_merge(self, lists: List[Optional[ListNode]], start, end) -> Optional[ListNode]:
        if start == end:
            return lists[start]
        elif start > end:
            return None
        elif start == end - 1:
            return self.merge(lists[start], lists[end])
        else:
            mid = (start + end) // 2
            list1 = self.help_merge(lists, start, mid)
            list2 = self.help_merge(lists, mid + 1, end)
            return self.merge(list1, list2)
    
    def merge(head1 : Optional[ListNode], head2 : Optional[ListNode]):
        if not head1:
            return head2
        if not head2:
            return head1
        cur = dummy = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next
        


