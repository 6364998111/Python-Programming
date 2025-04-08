n=int(input())
nu=64
for i in range(n):
    nu+=1
    for j in range(i+1):
        print(chr(nu),end=" ")
    print()
