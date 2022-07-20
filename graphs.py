


alist={}


edges=[(1,2),(2,3),(1,3),(2,4),(3,5),(5,4),(5,6),(4,6)]


for i in edges:
    if i[0] not in alist:
        alist[i[0]]=[]
    alist[i[0]].append(i[1])
    if i[1] not in alist:
        alist[i[1]]=[]
    alist[i[1]].append(i[0])


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

            
topological(alist)
print(alist)

