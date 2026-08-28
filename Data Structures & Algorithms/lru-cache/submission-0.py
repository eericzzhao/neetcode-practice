class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # maps the keys to the nodes
        self.cache = {}

        # dummy pointers, most recent/least recent accessed nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        # left = LRU, right = most recent
        self.left.next, self.right.prev = self.right, self.left

    # helper functions
    # remove node from list 
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert a node at the rightmost
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove it
            self.remove(self.cache[key])
            # we can reappend it to move it to the most recent position
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the cache/hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
