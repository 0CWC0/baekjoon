N=int(input())
for i in range(1,N+1):
    result=i
    for l in str(i):
        result+=int(l)
    if result==N:
        print(i)
        break
    elif i==N:
        print(0)
