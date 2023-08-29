def main():
    N,M=map(int,input().split()) #N은 바구니의 개수,번호 수
    n=0
    baskets=[]
    while n<N:
        baskets+=[0] #리스트 초기값 생성
        n+=1
    for basket in range(M):
        i,j,k=map(int,input().split())
        for num in range(i,j+1):
            baskets[num-1]=k

    for result in baskets:
        print(result,end=' ')



if __name__=='__main__':
    main()