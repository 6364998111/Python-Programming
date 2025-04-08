def smallest(arr):
    print("%.2f is the smallest element in the array."%min(arr))


arr=list(map(int,input().split()))
smallest(arr)