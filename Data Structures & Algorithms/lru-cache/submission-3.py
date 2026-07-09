class LRUCache:
    # Use hash for the retrieval 
    # Doubly linked list or deque so that least recently used put at the bottom
    # Hash is the pointer of the node so we can access and move at 0(1)
    # We can use ordereddict for this

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self._size = capacity
        self._dict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1

        # If key exist we should move it into the end
        self._dict.move_to_end(key)
        return self._dict[key]
    
    def put(self, key: int, value: int) -> None:
        # Case if the key exist, we just need to update the element, but if the key is not then we need to remove the least recently used
        if key in self._dict:
            self._dict.move_to_end(key)
        elif self._size == len(self._dict):
            self._dict.popitem(last=False)
        self._dict[key] = value
