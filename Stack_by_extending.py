class Stack(list):
    def is_empty(self):
        return len(self)==None
    def push(self,data):
        return self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")  
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise IndexError("Stack is empty")     
st1=Stack()
st1.push(30) 
st1.push(20) 
st1.push(700)
print("Element on top:",st1.peek())
print("remove element on top:",st1.pop())  
print("Element on top:",st1.peek())              
print()    