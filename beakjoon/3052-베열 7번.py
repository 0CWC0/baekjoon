def main():
    result=list()
    num=0
    for i in range(10):
        n=int(input())
        result+=[n%42]
    for i in set(result):
        num+=1
    print(num)
if __name__=='__main__':
    main()
    