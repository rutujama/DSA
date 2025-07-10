class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def enqueue(self,data=None):
        n=Node(data)
        if self.is_empty():
            self.front=n 
        else:
            self.rear.next=n 
        self.rear=n 
        self.item_count+=1 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:    
            self.front=self.front.next   
        self.item_count-=1    
    def get_front(self):
        if self.is_empty():
           raise IndexError("Queue is empty")   
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
           raise IndexError("Queue is empty")   
        else:
            return self.rear.item                  
    def size(self):
        return self.item_count
q=Queue()  
try:
    print(q.get_front())
except IndexError as e:
    print(e.args[0])      
q.enqueue(10)      
q.enqueue(30)                  
q.enqueue(60) 
q.enqueue(80) 
q.enqueue(20)
print("Front:",q.get_front(),"Rear:",q.get_rear())    