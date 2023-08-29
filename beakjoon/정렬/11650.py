N=int(input())
res=[]
for _ in range(N):
    x,y=list(map(int,input().split()))
    res.append([x,y])
res.sort() #x로 정렬하기
for i in sorted(res):
    print(*i)