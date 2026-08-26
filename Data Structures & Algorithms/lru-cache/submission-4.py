class ListNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def add(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == len(self.cache) and key not in self.cache:
            k = self.left.next
            self.remove(self.left.next)
            self.cache.pop(k.key)
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(self.cache[key])

