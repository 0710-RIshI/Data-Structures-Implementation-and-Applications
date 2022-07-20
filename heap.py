class Heap:
    def __init__(self):
        self.data=[]
    def heapinsert(self,value):
        self.data.append(value)
        i=len(self.data)-1
        while i>=1:
            j=i//2
            if j<1:
                break
            if(self.data[j]<self.data[i]):
                temp=self.data[j]
                self.data[j]=self.data[i]
                self.data[i]=temp
            i=i//2
        return self.data[1:]     
    def heapdelete(self):
        self.data[1]=self.data[len(self.data)-1]
        i=1
        while i<=len(self.data):
            if(i>=(len(self.data)-1)//2):
                break
            j=self.data[2*i]
            k=self.data[(2*i)+1]
            if j>k:
                temp=self.data[i]
                self.data[i]=self.data[2*i]
                self.data[2*i]=temp
                i=i+1
                continue
            else: #asuming j and k are not equal
                temp=self.data[i]
                self.data[i]=self.data[2*i+1]
                self.data[2*i+1]=temp
                i=i+1
                continue
            i=i+1
        size=len(self.data)-1
        self.data.pop()
        return self.data[1:size]
        
                
    


    
h=Heap()

h.data=[0]
print(h.heapinsert(10))
print(h.heapinsert(20))
print(h.heapinsert(15))
print(h.heapinsert(30))
print(h.heapinsert(40))
print(h.heapdelete())
print(h.heapdelete())
print(h.heapdelete())
print(h.heapdelete())



















    