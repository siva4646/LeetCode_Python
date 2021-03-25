class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(list)
        # print(self.map)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        items = self.map[key]
        low = 0
        high = len(items)
        
        while low < high:
            mid = (low + high) // 2
            if items[mid][0] > timestamp:
                high = mid
            else:
                low = mid + 1
        if low == 0:
            return ''
        return items[low-1][1]
            
            
            
            
            

    # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)