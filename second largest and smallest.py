def smallest(arr,n):
    if n <= 1:
        print(-1,-1)
    small=float('inf')
    second_small=float('inf')
    second_large=float('-inf')
    large=float('-inf')
    for i in range(n):
        small=min(small,arr[i])
        large=max(large,arr[i])
    for i in range(n):
        if arr[i] > small and arr[i] < second_small:
            second_small=arr[i]
        if arr[i] < large and arr[i] > second_large:
            second_large=arr[i]
    print(second_small,second_large)
    

arr=list(map(int,input().split()))
smallest(arr,len(arr))