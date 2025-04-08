n=int(input())
for i in range(n):
    if i == 0 or i%2 == 0:
        start = 0
    else:
        start = 1
    for i in range(i+1):
        if start == 0:
            print(1,end=" ")
            start = 1
        else:
            print(0,end=" ")
            start = 0
    print()
    