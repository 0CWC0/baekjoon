from itertools import product #중복 순얄
n,m=map(int,input().split())
for l in product([i for i in range(1,n+1)],repeat=m):
    print(*l,end='\n')