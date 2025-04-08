n=int(input())
left=1
right=n*2-1
for i in range(n):
    for j in range(1,n*2):
        if j >= left and j <= right:
            print("*",end="")
        else:
            print(" ",end="")
    left+=1
    right-=1
    print()
    