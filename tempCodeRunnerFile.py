from Singly_Linked_List import *
class Stack(SLL):
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_first(data)
    def pop(self):
        if not self.is_empty():
          self.delete_first()    
    def peek(self):
        if not self.is_empty():
            return self.start.item
    def size(self):
        return len(self)          
st1=Stack()
st1.push(30) 
st1.push(20) 
st1.push(700)
print("Element on top:",st1.peek())
print("remove element on top:",st1.pop())  
print("Element on top:",st1.peek())              
print()          