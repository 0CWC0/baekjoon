def hanoi(n,start,end):
    if n ==1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end) #1단계
    print(start,end) #2단계
    hanoi(n-1,6-start-end,end) #3단계


n=int(input()) #2**n-1 최소식
count=2**n-1
print(count)
hanoi(n,1,3)
