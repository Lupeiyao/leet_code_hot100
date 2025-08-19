from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        new_cur = dummy = Node(-1)
        old_cur = head
        node_dic = {}
        while old_cur:
            new_cur.next = Node(old_cur.val)
            node_dic.update({old_cur: new_cur.next})
            new_cur = new_cur.next
            old_cur = old_cur.next
        
        new_cur = dummy.next
        old_cur = head
        while old_cur:
            if old_cur.random:
                new_cur.random = node_dic.get(old_cur.random)
            new_cur = new_cur.next
            old_cur = old_cur.next

        return dummy.next
