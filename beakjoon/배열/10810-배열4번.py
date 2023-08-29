def main():
    alist=[]
    for i in range(9):
        n=int(input())
        alist.append(n)
    M=max(alist)
    print(M)
    print(alist.index(M)+1)

if __name__=='__main__':
    main()