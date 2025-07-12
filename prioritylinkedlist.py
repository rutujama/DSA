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
    def is_empty(self):
        return self.start is None

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.start.items
        self.start = self.start.next
        self.item_count -= 1
        return data    
    def size(self):
        return self.item_count

# Test
p = priorityQueue()
p.push("tiger", 1)
p.push("lion", 0)
p.push("elephant", 4)
p.push("dog", 3)
p.push("cat", 2)

while not p.is_empty():
    print(p.pop())