N=int(input())
answer=[]
for i in range(N//5+1):
    for j in range(N//3+1):
        if N-3*j-5*i==0:
            answer.append(i+j)
try:
    print(min(answer))
except ValueError:
    print(-1)