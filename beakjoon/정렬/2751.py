#수 정렬하기 2
N=int(input())
nums=[]
for i in range(N):
    nums.append(int(input()))
nums.sort()
for l in nums:
    print(l)