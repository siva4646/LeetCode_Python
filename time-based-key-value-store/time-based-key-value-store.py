class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))
        # print(self.map)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        items = self.map[key]
        low = 0 
        right = len(items) 
        while low < right:
            mid = (low + right) // 2
            if items[mid][0] > timestamp:
                right = mid
            else:
                low = mid + 1
        if low == 0:
            return ''
        return items[low - 1][1] 
            
            
            
            
            

    # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)