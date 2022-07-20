



class Node:
    def __init__(self):
        self.data=0
        self.next=None

class queue:
    head=Node()
    tail=Node()
    def __init__(self):
        self.head=None
        self.tail=None
    
    def isempty(self):
        if self.head==None or self.tail==None:
            return True
        else:
            return False
    

    def enqueue(self,value):
        n = Node()
        n.data=value
        if self.isempty():
            self.head=n
            
        else:
            while self.tail.next!=None:
                self.tail=self.tail.next
        self.tail=n
        print(f"enqueue successful {self.tail.data}")
    
    def dequeue(self):
        if self.isempty():
            print("queue is empty")
        else:
            self.head=self.head.next
        
    def displayqueue(self):
        y = Node()
        y=self.head
        while y.data!=None:
            print(y.data,sep='\n')
            y=y.next
        
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.displayqueue()
q.displayqueue()








    
        

