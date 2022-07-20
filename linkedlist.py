class node:
    def __init__ (self,item):
        self.data = item
        self.ref = None
class linkedlist:
    def __init__(self):
        self.head = None

    def insert_start(self,item):
        newnode = node(item)
        newnode.ref=self.head
        self.head=newnode

    def insert_end(self,item):
        newnode = node(item)
        if self.head== None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None :
                n=n.ref
            n.ref=newnode

    def insert_after_item(self,a,item):
        n=self.head
        while n is not None:
            n=n.ref
            if(n.data==a):
                break
        if(n is None):
                print("error ...Item not in the list ")
        else:
            newnode=node(item)
            newnode.ref=n.ref
            n.ref=newnode

    def insert_before_item(self,item,b):
        n=self.head
        if n.ref == None:
            print("list has no element")
        else:
            while n is not None :
                if(n.ref.data==b):
                    break
                n=n.ref
            if(n==None):
                print("error ... Item not in the list")
            else:
                newnode=node(item)
                newnode.ref=n.ref
                n.ref=newnode

    def insert_index(self,item,index):
        i=0
        if(index==0):
            newnode = node(item)
            newnode.ref=self.head
            self.head=newnode
        else:
            n=self.head
            while n is not None :
                if i==index-1:
                    break
                i+=1
                n=n.ref
            if(n==None):
                print("error ... index overflow")
            else:
                newnode=node(item)
                newnode.ref=n.ref
                n.ref=newnode
  
    def traverse(self):
        if self.head is None :
            print("list has no element")
        else :
            n=self.head
            while n is not None:
                print(n.data," ")
                n=n.ref

    def delete_start(self):
        if self.head is None:
            print("error...The list has no element")
            return
        self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("error...The list has no element")
            return
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        p=n.ref.data
        n.ref=None
        return p

    def delete_value(self,val):
        if self.head is None:
            print("error...The list has no element")
            return
        elif self.head==val:
            self.head =self.head.ref
            return
        else:
            n=self.head
            while n is not None:
                if n.data==val:
                    break
                n=n.ref
            if n is None:
                    print("error ...the item is not in the list")
            else:
                p=n.ref.data
                n.ref=n.ref.ref
            
    def search(self,val):
        n=self.head
        while n is not None:
            if n.data==val:
                print("item found")
                return 1
            n=n.ref
        if n is None:
            print("item not found ")
            return 0
