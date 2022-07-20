def quicksort(arr,low,high):
    print(arr)
    if(low<high):
       crt=partition(arr,low,high)
       quicksort(arr,low,crt-1)
       quicksort(arr,crt+1,high)

def partition(arr,low,high):
    pivot=low
    i=low
    j=high
    while(i<j):
        while(arr[i]<=arr[pivot] and i<high):
            i+=1
        while(arr[j]>arr[pivot] and j>low):
            j-=1
        
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[pivot]
    arr[pivot]=arr[j]
    arr[j]=temp

    return j

#driver code

list=[5,1,4,3,6,9,2]
quicksort(list,0,len(list)-1)












        

