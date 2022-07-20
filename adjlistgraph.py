class stack():
    def __init__(self):
        self.l=[]
    def push(self,value):
        self.l.append(value)
    def pop(self):
        return self.l.pop(len(self.l)-1)
    def isempty(self):
        if len(self.l==0):
            return True
        else:
            return False

visited=[]


def neighbour(x):
    return alist[x]



def bfs(key):
    s=stack()
    s.push(key)
    while len(s.l)!=0:
        temp=s.pop()
        print(temp,end='\t')
        for j in alist[temp]:
            s.push(j)

def dfs(key):
    m=[]
    m.append(key)
    while len(m)!=0:
        temp=m.pop(0)
        print(temp,end='\t')
        for j in alist[temp]:
            m.append(j)

def haspath(x,y):
    
    flag=0
    s=stack()
    s.push(x)
    while len(s.l)!=0:
        temp=s.pop()
        visited.append(temp)
        if temp==y:
            flag=1
            print("Yes")
            break
        elif temp in visited:
            continue
        else:
            for j in alist[temp]:
                s.push(j)
    if flag==0:
        print("No")


       

dfs('a')
haspath('a','f')

