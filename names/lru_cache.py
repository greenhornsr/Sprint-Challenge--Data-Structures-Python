import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10001):
        self.limit = limit
        # current number of nodes being held
        self.size = 0
        # doubly linked list
        self.dbl_list = DoublyLinkedList()
        # storage ----> dictionary <----
        self.cache_storage = {}
    
    def __str__(self):
        f"{self.limit}, {self.size}, {self.cache_storage}"

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # tuple
    '''
    0     1
    (key, value)
    '''

    def get(self, key):
        if key in self.cache_storage:
            curr_node = self.cache_storage[key]
            self.dbl_list.move_to_end(curr_node)
            return curr_node.value[1]
        else:
            return None
        
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache_storage:
            node = self.cache_storage[key]
            node.value = (key, value)
            self.dbl_list.move_to_end(node)
            return
        
        if self.size == self.limit:
            del self.cache_storage[self.dbl_list.head.value[0]]
            self.dbl_list.remove_from_head()
            self.size -= 1

        
        self.dbl_list.add_to_tail((key, value))
        self.cache_storage[key] = self.dbl_list.tail
        self.size += 1


# l = LRUCache()
# print(l.get('test'))