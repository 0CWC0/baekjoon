import sys
input=sys.stdin.readline

n=int(input())
array=[]
for _ in range(n):
    x,y=map(int,input().split())
    array.append([y,x]) #담을 때도 바꿔서 담아서 sort는 y기준

res_array=sorted(array)
for x,y in res_array:
    print(y,x) #좌우 반전으로 출력

#두 번째 답안
#for i in range(n):
#   print(res_array[i][1],res_array[i][0])
