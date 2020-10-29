"""Define class Node."""


class Node:
    """Define Node class to track node properties."""

    def __init__(self, data):
        """Set Node properties."""
        self.data = data
        self.next = None
        self.previous = None
