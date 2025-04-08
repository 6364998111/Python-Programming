n=int(input())
l=n
k=l
for i in range(n):
    for j in range(1,(n*2)):
        if j >= k and j <= l:
            print('*',end='')
        else:
            print(' ',end='')
    k-=1
    l+=1
    print()
l=1
k=n*2-1
for i in range(n):
    for j in range(1,n*2):
        if j >= l and j <= k:
            print("*",end="")
        else:
            print(" ",end="")
    l+=1
    k-=1
    print()