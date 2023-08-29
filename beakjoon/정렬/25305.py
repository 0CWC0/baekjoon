# 커트라인
N,K=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
print(x[N-K])