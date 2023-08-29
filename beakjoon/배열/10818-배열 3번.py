def main():
    N=int(input())
    nlist=[]
    for i in range(N):
        nlist+=[0]
    nlist=list(map(int,input().split()))
    print(min(nlist),max(nlist),end=' ')


if __name__=='__main__':
    main()