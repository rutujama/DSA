class Node():
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
# Update to trigger Git tracking

class SLL():
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        if self.start.item == data:
            self.start = self.start.next
            return
        temp = self.start
        while temp.next is not None:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next
class SLLiterable():
    def __init__(self,start):
        self.current=start
    def __iter__(self): 
        return self
    def next(self):
        if not self.start:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
                            
mylist=SLL()
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(20)
print()
mylist.print_list()
print()