class Queue():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0 
    def enqueue(self,data):
        self.items.append(data)