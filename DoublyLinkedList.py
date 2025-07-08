class Node():
    def __init__(self, prev=None, next=None, item=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL():
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n = Node(None, self.start, data)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        if self.start is None:
            self.start = Node(None, None, data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, None, data)
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, temp.next, data)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
        
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    def __iter__(self):
        return DLLiterator(self.start)

class DLLiterator():
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# ---------------- Test the DLL ----------------

mylist = DLL()
mylist.insert_at_first(30)
mylist.insert_at_first(70)
mylist.insert_at_last(90)
mylist.insert_after(mylist.search(30), 80)
mylist.print_list()  # Output: 70 30 80 90

print("Using iterator:")
for item in mylist:
    print(item, end=' ')
