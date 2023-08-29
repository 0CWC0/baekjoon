N=int(input())
numbers=[]
for i in range(N):
    numbers.append(int(input()))
numbers.sort()
#result=sorted(numbers,reverse=True) #역순
for l in numbers:
    print(l)