from Singly_Linked_List import *
class Stack(SLL):
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_first(data)
    def pop(self):
        if not self.is_empty():
          self.delete_first()    