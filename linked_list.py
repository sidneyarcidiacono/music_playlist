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
        self.tail = node
        if self.head is None:
            self.head = node

    def prepend(self, data):
        """Create a new Node and prepend to list."""
        node = Node(data)
        if self.head is not None:
            self.head.previous = node
            node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
            self.tail.next = None
            self.tail.previous = None

    def print_songs(self):
        """Print all 'songs' (nodes) in list."""
        current = self.head
        while current is not None:
            print(current.data)
            current = self.next

    def delete_from_head(self):
        """Delete item from head."""
        self.head = self.head.next

    def delete_from_tail(self):
        """Delete item from tail."""
        self.tail.previous = self.tail
        self.tail.next = None
