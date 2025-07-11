from Singly_Linked_List import *
class Stack():
    def __init__(self):
        self.sll=SLL()
        self.item_count=0
    def is_empty(self):
        return self.sll.is_empty()
    def push(self,data):
        self.sll.insert_at_first(data)   
        self.item_count+=1 
    def pop(self):
        if not self.is_empty():
           self.sll.delete_first()    
           self.item_count-=1 
    def peek(self):
        if not self.is_empty():
            return self.sll.start.item 
    def size(self):
        return self.item_count 