class Doublyll:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = Doublyll(0, 0)
        self.end = Doublyll(0, 0, None, self.head)
        self.head.next = self.end

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        if node:
            self.remove_node(node)
            self.add_node_to_start(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])

        node = Doublyll(key, value)
        self.hashmap[key] = node
        self.add_node_to_start(node)

        if len(self.hashmap) > self.capacity:
            lru = self.end.prev
            self.remove_node(lru)
            del self.hashmap[lru.key]

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node_to_start(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node




