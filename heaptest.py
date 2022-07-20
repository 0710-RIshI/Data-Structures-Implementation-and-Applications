
def heapify(heapdata):
    n=len(heapdata)-1
    i=n
    while i>=1:
        if heapdata[i]>heapdata[i//2]:
            (heapdata[i],heapdata[i//2])=(heapdata[i//2],heapdata[i])
        i=i//2
    return heapdata

sorted=[]

def insert(value,heapdata):
    heapdata.append(value)
    heapdata=heapify(heapdata)
    return heapdata
    
def delete(x):
    n=len(x)-1
    print("element to be popped",x[0])
    (x[0],x[n])=(x[n],x[0])
    print(x)
    sorted.append(x[n])
    x.pop(n)
  
   
    i=0
    while i<len(x):
        if i>=(len(x)-1)//2:
            break
        if max(x[2*i+2],x[2*i+1])>x[i]:
            if x[2*i+2]<x[2*i+1]:
                (x[i],x[2*i+1])=(x[2*i+1],x[i])
                i=i+1
                continue
            else:
                (x[i],x[2*i+2])=(x[2*i+2],x[i])
                i=i+1
                continue
        i=i+1
    

    
    print(x[:n])

    def topological(AList):
    indegree = {i:0 for i in range(10)}
    path = {i:0 for i in range(10)}
    for i in AList:
        for j in AList[i]:
            indegree[j] += 1
    
    while indegree:
        l = min([i for i in indegree if not indegree[i]])
        indegree.pop(l)
        print(l,end=" ")
        if l in AList:
            for i in AList[l]:
                indegree[i] -= 1
                path[i] = max(path[i], path[l]+1)
    print(path)

            
topological(adj_list)def topological(AList):
    indegree = {i:0 for i in range(10)}
    path = {i:0 for i in range(10)}
    for i in AList:
        for j in AList[i]:
            indegree[j] += 1
    
    while indegree:
        l = min([i for i in indegree if not indegree[i]])
        indegree.pop(l)
        print(l,end=" ")
        if l in AList:
            for i in AList[l]:
                indegree[i] -= 1
                path[i] = max(path[i], path[l]+1)
    print(path)

            
topological(adj_list)

heapdata=[0,100,40,50,20,15,30,35]
heapdata=insert(55,heapdata[1:])
print(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
delete(heapdata)
print(sorted)


    


    



