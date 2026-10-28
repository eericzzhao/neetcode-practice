# We want to start off by creating a Node class so we can actually ahve something that we can cache
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        
        # map from the key to the nodes
        self.LRUCache = {}

        # dummy nodes to store the most recently used node vs the least reecntly used node 
        # lru (left ) vs mru (right) 
        self.lru, self.mru = Node(0,0), Node(0,0)
        # now to connect them to eachother
        self.lru.next, self.mru.prev = self.mru, self.lru 
    
    # helper functions 
    # remove helper
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    # insert helper
    def insert(self, node):
        # prev is our actual mr added node, nxt contains the dummy
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            # because we're accessing it, we need to remove and add back
            self.remove(self.LRUCache[key])
            self.insert(self.LRUCache[key])
            return self.LRUCache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])

        # we want to update our mapping so that theis key has the node
        self.LRUCache[key] = Node(key, value)
        self.insert(self.LRUCache[key])
        if len(self.LRUCache) > self.size:
            lru = self.lru.next
            self.remove(lru)
            del self.LRUCache[lru.key]
        
