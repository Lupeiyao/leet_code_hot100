from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 获取两个链表相交的节点
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        a_size, b_size, tmpA, tmpB = 1, 1, headA, headB
        while tmpA.next is not None:
            a_size += 1
            tmpA = tmpA.next
        while tmpB.next is not None:
            b_size += 1
            tmpB = tmpB.next
        if tmpA != tmpB:
            return None
        if a_size > b_size:
            long_head, short_head = headA, headB
        else:
            long_head, short_head = headB, headA
        for _ in range(abs(a_size - b_size)):
            long_head = long_head.next
        while long_head != short_head:
            long_head = long_head.next
            short_head = short_head.next
        return long_head

    # 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = None
        while head is not None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    # 判断回文链表
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        list = []
        while head is not None:
            list.append(head.val)
            head = head.next
        start, end = 0, len(list) - 1
        while start <= end:
            if list[start] != list[end]:
                return False
            start += 1
            end -= 1
        return True

    # 判断是否有环
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 返回有环链表的入环节点
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        node_set = set()
        while head:
            if head in node_set:
                return head
            else:
                node_set.add(head)
            head = head.next
        return None

    # 合并两个升序list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        cur = dummy = ListNode(1)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next

    # 求和
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cur = dummy = ListNode(0)
        pre = 0
        while l1 or l2:
            val = pre
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            pre = val // 10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next
        if pre > 0:
            cur.next = ListNode(pre)
        return dummy.next

    # 删除倒数第N个节点
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    # 两两交换相邻的节点
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = head
            pre.next = next
            pre = head
            head = head.next
        return dummy.next




