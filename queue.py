class Queue():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0 
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0] 
        else:
            raise IndexError("queue is empty")     
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
            raise IndexError("queue is empty")    
    def size(self):
        return len(self.items)
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
try:
    print(q.dequeue())
    print("Number of element in queue:",q.size())
except IndexError as e:
    print(e.args[0])                           