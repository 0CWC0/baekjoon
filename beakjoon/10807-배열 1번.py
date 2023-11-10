def main():
    N=int(input())
    alist=[]

    for i in range(N):
        alist+=[0]
    print(alist)
    alist=list(map(int,input().split()))
    print(alist)
    v=int(input())
    print(alist.count(v))

main()