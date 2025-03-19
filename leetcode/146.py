class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        
        # We'll keep a sentinel tail node. The "head" pointer is for the most recently used node.
        self.tail = Node(-1, -1)  # Sentinel tail
        self.head = None         # Will point to the most recently used (MRU) node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        
        # If it's already at the head (most recently used), just return it
        if node == self.head:
            return node.val
        
        # Unlink it from its current position
        self._remove_node(node)
        
        # Move it to the head
        self._move_to_head(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        # 1) If the key already exists, update and move to head
        if key in self.dict:
            node = self.dict[key]
            node.val = value  # update value
            if node != self.head:
                self._remove_node(node)
                self._move_to_head(node)
            return
        
        # 2) Otherwise, it's a new key. Create a new node and add it to head
        new_node = Node(key, value)
        self.dict[key] = new_node
        
        # If this is the very first real node, link it with the sentinel tail
        if not self.head:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self._move_to_head(new_node)
        
        # 3) If we exceed capacity, we must evict from tail
        if len(self.dict) > self.capacity:
            self._evict_from_tail()

    def _evict_from_tail(self):
        """Remove the least recently used item, which is the node directly before self.tail."""
        to_evict = self.tail.prev
        if not to_evict:  # If there's nothing before tail, just return
            return
        
        # Unlink from the dictionary
        del self.dict[to_evict.key]
        
        # Unlink from the list
        prev_node = to_evict.prev
        if prev_node:
            prev_node.next = self.tail
        self.tail.prev = prev_node
        
        # If we evicted the only node in the list, update self.head to None
        if to_evict == self.head:
            # That means there are no real nodes left
            self.head = None

    def _remove_node(self, node: Node):
        """Remove an existing node from the list (not from the dictionary)."""
        prev_node = node.prev
        next_node = node.next
        
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        
        # If the node was head, update head
        if node == self.head:
            # The 'next_node' might be the sentinel tail or None
            self.head = next_node if (next_node != self.tail) else None

        node.prev = None
        node.next = None

    def _move_to_head(self, node: Node):
        """Place 'node' at the head (most recently used) position."""
        # If there's no head yet, just set head to node and link node<->tail
        if not self.head:
            self.head = node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        
        # Otherwise, set the new node in front of the old head
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def print_list(self):
        """Debug method: print the doubly linked list forward and backward."""
        print("Forward list:")
        current = self.head
        while current:
            print(f"[{current.key}={current.val}]", end=" -> ")
            current = current.next
        print("None")

        print("Backward list:")
        current = self.tail
        while current:
            print(f"[{current.key}={current.val}]", end=" -> ")
            current = current.prev
        print("None\n")

