class Node():
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 
class Stack():
    def __init__(self):
        self.start=None
        self.item_count=0 
    def is_empty(self):
        return self.start==None 