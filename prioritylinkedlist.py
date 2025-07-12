class Node:
    def __init__(self, items=None, priority=None):
        self.items = items
        self.priority = priority
        self.next = None

class priorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0