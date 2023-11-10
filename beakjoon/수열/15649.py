import sys
from itertools import permutations #순열(순서가 다를때 경우의 수로 인정)
input=sys.stdin.readline
n,m=map(int,input().split())
nums=[i for i in range(1,n+1)]
for i in permutations(nums,m):
    print(i)
##제너레이터로 구현하는 조합
def combinations_2(array,r):
    for i in range(len(array)):
        if r==1: # 종료조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:],r-1):#리스트 인덱싱
                yield [array[i]] + next
for i in combinations_2([1,2,3,4],3):
    print(i,end=' ')
