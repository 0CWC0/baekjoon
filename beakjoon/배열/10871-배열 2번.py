def main():
    N,X=map(int,input().split())
    A=[]
    for i in range(N):
        A+=[0]
    A=list(map(int,input().split()))
    for i in A :
        if i<X:
            print(i,end=' ')

if __name__=='__main__':
    main()