import sys
input=sys.stdin.readline
N=int(input())
infos=[]

for i in range(N):
    age,name=input().split()
    infos.append([int(age),name])
for l in sorted(infos,key=lambda x:x[0]):
    print(*l)
