class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0 
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if self.is_empty():
            self.rear=n 
        else:
            self.front.prev=n 
        self.front=n 
        self.item_count+=1   
    def insert_rear(self,data):
        n=Node(self.rear,data,None)
        if self.is_empty():
            self.front=n 
        else:
            self.rear.next=n 
        self.rear=n 
        self.item_count+=1    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        elif self.front==self.rear:
            self.front=None 
        else:
            self.front=self.front.next 
            self.front.prev=None 
        self.item_count-=1     
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        elif self.front==self.rear:
            self.rear=None 
        else:
            self.rear=self.rear.prev
            self.rear.next=None 
        self.item_count-=1        
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.front.item 
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.rear.item      