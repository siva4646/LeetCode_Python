class Node:
    def __init__(self, key, val):
        # instances
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.dic) == self.capacity:
                tailPrev = self.tail.prev
                self.remove(tailPrev)
                del self.dic[tailPrev.key]
            newNode = Node(key, value)
            self.add(newNode)
            self.dic[key] = newNode
            
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

         
        
              
        
        
        # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)