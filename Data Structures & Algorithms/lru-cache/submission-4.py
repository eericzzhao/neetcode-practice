class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity

        # in order to easily access doubly-linked list, we should have a map
        self.LRUcache = {}

        # dummy nodes for the lru vs mru
        self.lru, self.mru = Node(0,0), Node(0,0)

        self.lru.next, self.mru.prev = self.mru, self.lru
    
    # helper functions 
    # remove helper
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert helper 
    def insert(self, node):
        # insert starts at the rightmost side
        rightMostNode, boundary = self.mru.prev, self.mru
        rightMostNode.next = boundary.prev = node
        node.prev, node.next = rightMostNode, boundary

    def get(self, key: int) -> int:
        # if its a node we see already, then, we need to move it to the MRU side (rightmost)
        if key in self.LRUcache:
            self.remove(self.LRUcache[key])
            self.insert(self.LRUcache[key])
            return self.LRUcache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # we need to remove this node if it exists already because we're accessing it
        if key in self.LRUcache:
            self.remove(self.LRUcache[key])
        
        # either way, we still need to recreate the Node
        # this way we can not only creat a new node, we can assign it a key in the lrucache map
        self.LRUcache[key] = Node(key, value)
        # we need to move it as its a most recently used node 
        self.insert(self.LRUcache[key])

        if len(self.LRUcache) > self.size:
            # we need tomoreve a LRU node
            leastAccessedNode = self.lru.next
            self.remove(leastAccessedNode)
            
            del self.LRUcache[leastAccessedNode.key]


        
        
