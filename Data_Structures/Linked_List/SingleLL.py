class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:                                  # Empty LL
            print('LinkedList is Empty')
            return
        
        ptr=self.head                                          # Non Empty LL
        while ptr:
            print(ptr.data)
            ptr=ptr.next
            

if __name__ == '__main__':
    ll=LinkedList()                                       # in ML model=DecisionttreeRegressor() -> ceating object of a class
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.print()