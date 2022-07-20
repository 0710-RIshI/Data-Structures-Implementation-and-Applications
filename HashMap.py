values=[]

def hashfn(k,n):
    index=k%n

    if values[index]==0:
        values[index]=k
    else:
        i=index
        while values[i]!=0:
            if i==n-1:
                i=0
            i=i+1
        values[i]=k    
    
print("enter size:")
size=int(input())

for i in range(size):
    values.append(0)
for i in range(10):
    print("enter value:",(i+1))
    x=int(input())
    hashfn(x,size)
print("Index\tvalues")
for i in range(len(values)):
    if values[i]!=0:
        print(i,values[i],end='\n',sep='\t')

        
    




