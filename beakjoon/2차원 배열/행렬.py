def main():
    #2738
    """N,M=map(int,input().split())
    A=[ list(map(int, input().split())) for i in range(N)]
    B=[list(map(int, input().split())) for i in range(N)]
    result=[[0 for j in range(M)] for i in range(N)]
    for n in range(N):
        for j in range(M):
            result[n][j]=A[n][j]+B[n][j]
    for resu in result:
        print(*resu)

    #2566
    import random
    board=[list(map(int,input().split())) for i in range(9)]
    count=0
    choice=[]
    max_list=[max(n) for n in board]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if max(max_list)==board[row][col]:
                count += 1
                choice+=[0]
                choice[count-1] = [row + 1,board[row].index(max(max_list))+1]
    print(max(max_list))
    if count==1:
        print(*choice[0])
    else:
        print(*random.choice(choice))


    #10798
    s_list=[]
    elem_list=[]
    string=''
    for i in range(5):
        s_list+=[0]
        s_list[i]=input()
        elem_list+=[len(s_list[i])]
    result=[""]* max(elem_list)
    for j in range(len(s_list)):
        for n in range(len(s_list[j])):
            result[n]+=s_list[j][n]
    for res in result:
        string+=res
    print(string)"""


    #2563
    paper=[[0 for l in range(100)] for i in range(100)]
    paper_num=int(input())
    result=0
    for num in range(paper_num):
        paper_pos=list(map(int,input().split()))
        for i in range(10):
            for j in range(10):
                paper[paper_pos[0]+i][paper_pos[1]+j]=1
    for x in range(100):
        for y in range(100):
            if paper[x][y]==1:
                result+=1
    print(result)
if __name__=="__main__":
    main()