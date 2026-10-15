class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.tail.prev = self.head
        self.head.nxt = self.tail
    
    def remove(self,node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
    
    def add(self, key, value):
        node = Node(key,value)

        node.nxt = self.head.nxt
        self.head.nxt = node
        node.nxt.prev = node
        node.prev = self.head
        return node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        new_node = self.add(key, node.value)
        self.cache[key] = new_node
        return new_node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = self.add(key,value)
        self.cache[key] = new_node

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


