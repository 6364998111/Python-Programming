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