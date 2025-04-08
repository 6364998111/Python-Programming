def partition(arr,low,high):
    pi=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pi:
            i+=1
        while arr[j]>pi:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quicksort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr=[1,5,3,8,2,9]
quicksort(arr,0,len(arr)-1)
print(arr)
