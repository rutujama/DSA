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
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")    
        else:
            return self.items[0]       
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")    
        else:
            return self.items[-1]     
    def size(self):
        return len(self.items)   
q=Deque()
q.insert_front(30) 
q.insert_front(100) 
q.insert_front(90) 
q.insert_rear(50) 
q.insert_rear(200)    
print("Front:",q.get_front(),"Rear:",q.get_rear())
print("Number of element in queue:",q.size())               