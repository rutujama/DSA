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