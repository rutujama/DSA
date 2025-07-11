class Stack(list):
    def is_empty(self):
        return len(self)==None
    def push(self,data):
        return self.append(data)