"""Import node."""
from node import Node


class LinkedList:
    """Define Linked List class to track nodes."""

    def __init__(self):
        """Define Linked List properties."""
        self.head = None
        self.tail = None

    def append(self, data):
        """Create a new Node and append to list."""
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
            node.previous = self.tail
            node.next = None
            self.tail = node
        if self.head is None:
            self.head = node
        self.tail = node

    def prepend(self, data):
        """Create a new Node and prepend to list."""
        node = Node(data)
        if self.head is not None:
            self.head.previous = node
            node.next = self.head
        if self.tail is None:
            self.tail = node
            self.tail.next = None
            self.tail.previous = None
        self.head = node
        self.head.previous = None

    def print_songs(self):
        """Print all 'songs' (nodes) in list."""
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_from_head(self):
        """Delete item from head."""
        self.head = self.head.next

    def delete_from_tail(self):
        """Delete item from tail."""
        self.tail = self.tail.previous
        self.tail.next = None

    def delete(self, item):
        """Delete item from anywhere in list."""
        current = self.head
        while current is not None:
            if current.data is item:
                if current.next is not None and current.previous is not None:
                    current = current.previous
                    current.next = current.next.next
                elif current.next.next is None:
                    current = current.previous
                    current.next = None
                    self.tail = current
                elif current.previous is None:
                    self.head = current.next
                    self.head.next = current.next.next
                break
            else:
                current = current.next

    def find(self, item):
        """Find specific item in list."""
        current = self.head
        found = False
        while current is not None:
            if current.data is not item:
                current = current.next
            elif current.data is item:
                found = True
            return found

    def reverse(self):
        """Reverse order of list."""
        next = None
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
