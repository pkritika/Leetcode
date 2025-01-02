class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [None for _ in range(self.size)]  #To create empty bucket

    def _index(self,key): 
        return key % self.size




    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.bucket[idx]:
            self.bucket[idx] = ListNode(key, value)
            return
        current = self.bucket[idx]
        while current:
            if current.key == key:  # Update value if key exists
                current.value = value
                return
            if not current.next:  # Add a new node at the end
                current.next = ListNode(key, value)
                return
            current = current.next
    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.bucket[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.bucket[idx]
        if not current:
            return
        if current.key == key:
            self.bucket[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)