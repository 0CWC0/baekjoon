"""n,k=map(int,input().split()) #n개의 집합에서 순서없이 k 개의 수를 고르는 조합의 수
def fact(l):#n 팩토리얼 구하기
    num=1
    for i in range(2,l+1):
        num*=i
    return num
print(int( fact(n)/(fact(n-k)*fact(k) ))) #n!/(n-k)!*k!"""

#다리 놓기 1010
def fact(l): #n 팩토리얼 구하기
    num=1
    for i in range(2,l+1):
        num*=i
    return num

for _ in range(int(input())):
    west,east=map(int,input().split())
    print(fact(east)//(fact(west)*fact(east-west)))