def main():
    N=int(input())
    alist=[]
    """alist=[]
    alist=list(map(int,input().split()))
    if len(alist)==N:
        v=int(input())
        print(alist.count(v))"""
    for i in range(N):
        alist+=[0]
    print(alist)
    alist=list(map(int,input().split()))
    print(alist)
    v=int(input())
    print(alist.count(v))

main()