T=int(input()) #테스트 케이스의 개수
for i in range(T):
    C=int(input()) #센트
    Q=C//25
    D=(C-Q*25)//10
    N=(C-Q*25-D*10)//5
    P=(C-Q*25-D*10-N*5)//1
    print(Q,D,N,P)