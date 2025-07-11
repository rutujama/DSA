class Stack():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==None 
    def push(self,data):
        if not self.is_empty():
            return self.items.append(data)
        else:
            raise IndexError("Stack is empty")
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)          