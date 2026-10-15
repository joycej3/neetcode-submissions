class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        

    def remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def add_node(self,key,value):
        node = Node(key,value)

        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt = node
        node.nxt.prev = node
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # its in key
        #remove it from list and add it back
        node = self.cache[key]
        self.remove_node(node)
        new_node = self.add_node(node.key, node.value)
        self.cache[key] = new_node
        return node.value   

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        new_node = self.add_node(key,value)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity: 
            lru = self.tail.prev
            self.remove_node(lru)
            del(self.cache[lru.key])
        
