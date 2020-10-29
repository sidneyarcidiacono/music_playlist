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
        self.tail = node
        if self.head is None:
            self.head = node

    def prepend(self, data):
        """Create a new Node and prepend to list."""
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
