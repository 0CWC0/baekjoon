import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split())) #n개의 숫자
m=int(input())
m_num=list(map(int,input().split())) #m개의 숫자
for i in range(len(m_num)):
    if m_num[i] in num:
        m_num[i]=1
    else:
        m_num[i] = 0
print(*m_num)