class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        value = self.table.pop(key)
        self.table[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table.pop(key)
        elif len(self.table) >= self.capacity:
            # Find the very first key (LRU) and delete it
            oldest_key = next(iter(self.table))
            del self.table[oldest_key]
            
        self.table[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
