class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data) 
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")    
        else:
            self.items.pop[0]
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")    
        else:
            self.items.pop[-1]    