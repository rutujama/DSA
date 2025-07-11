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
st1=Stack()
st1.push(30) 
st1.push(20) 
st1.push(700)
print("Element on top:",st1.peek())
print("remove element on top:",st1.pop())  
print("Element on top:",st1.peek())              
print()    