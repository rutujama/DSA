class Node:
    def __init__(self, items=None, priority=None):
        self.items = items
        self.priority = priority
        self.next = None

class priorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1    