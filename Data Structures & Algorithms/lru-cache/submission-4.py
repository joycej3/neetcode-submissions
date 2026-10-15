class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.head.nxt = self.tail
        self.tail.prev = self.head



    def remove_node(self, node):
        p, n = node.prev, node.nxt
        p.nxt = node.nxt
        n.prev = node.prev
    
    def add_node(self, key,val):
        node = Node(key, val)
        node.nxt = self.head.nxt
        self.head.nxt.prev = node
        self.head.nxt = node
        node.prev = self.head
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        
        new_node = self.add_node(node.key, node.val)
        self.cache[key] = new_node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
            del self.cache[key]


        if self.cap == len(self.cache):
            lru = self.tail.prev
            self.remove_node(self.tail.prev)
            del self.cache[lru.key]

        node = self.add_node(key, value)
        self.cache[key] = node
        
        

