N,M=map(int,input().split())
board=[]
result=[]
for _ in range(N):
    board.append(input()) #append 로 추가, 기존에 리스트 공간 명시할 필요 X

for i in range(N-7): #시작점 찾기
    for j in range(M-7): #흑백을 위해 2개의 좌표 지정
        draw1=0
        draw2=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b] != 'B':
                        draw1+=1
                    if board[a][b] !='W':
                        draw2 +=1
                else:
                    if board[a][b] != 'W':
                        draw1+=1
                    if board[a][b] != 'B':
                        draw2+=1
        result.append(draw1)
        result.append(draw2)

print(min(result))