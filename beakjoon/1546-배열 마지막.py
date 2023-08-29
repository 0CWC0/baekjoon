def main():
    N=int(input())
    score=[]
    sum=0
    for i in range(N):
        score+=[0]
    score=list(map(int,input().split()))
    M=max(score)
    for elem in score: #점수 고치기
        elem=elem/M*100
        sum+=elem
    print(sum/N)
if __name__=='__main__':
    main()