class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.addToHead(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.addToHead(node)
            
        else:
            if len(self.dic) == self.capacity:
                tailPrev = self.tail.prev
                self.remove(tailPrev)
                del self.dic[tailPrev.key]
                
            newNode = Node(key, value)
            self.addToHead(newNode)
            self.dic[key] = newNode   

    def addToHead(self, node): # most recently used
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
         


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)