
class DListNode:

    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.dummy_head = DListNode(-1)
        self.dummy_tail = DListNode(-1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head
        self.size = 0
        

    def get(self, key: int) -> int:
        result = -1
        if key in self.cache:
            result = self.cache[key].val
            self.move_head(self.cache[key])
        return result
    
    def move_head(self, node : DListNode):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.add_to_head(node)
        

    def add_to_head(self, node : DListNode):
        node.next = self.dummy_head.next
        node.pre = self.dummy_head
        self.dummy_head.next.pre = node
        self.dummy_head.next = node

    def remove_tail(self):
        result = self.dummy_tail.pre.key
        self.dummy_tail.pre.pre.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_tail.pre.pre
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_head(self.cache[key])
        else:
            node = DListNode(value, key)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                remove_key = self.remove_tail()
                self.cache.pop(remove_key)
                self.size -= 1