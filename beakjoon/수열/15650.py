from itertools import combinations #조합
n,m=map(int,input().split())
for i in combinations([i for i in range(1,n+1)],m): #m개의 수를 객체에서 중복없이 뽑아냄
    print(*i)

def combinations_2(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for l in combinations_2(array[i:],r-1):
                yield [array[i]] +l
for i in combinations_2([1,2,3,4],2):
    print(i,end=' ')