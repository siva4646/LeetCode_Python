class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True
        
            
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            last_element, idx = self.list[-1], self.dic[val]
            self.list[idx], self.dic[last_element] = last_element, idx
            self.list.pop()
            del self.dic[val]
            return True
        return False
  
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
 
        

#https://www.youtube.com/watch?v=ufsUFkbypsc&ab_channel=thecodingworld

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()