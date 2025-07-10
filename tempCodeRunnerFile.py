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