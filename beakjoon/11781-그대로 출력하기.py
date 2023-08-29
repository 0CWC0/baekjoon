def main():
    result=0
    s=input().split()
    for i in s:
        if type(i)!=type(str):
            result+=1
    print(result)
main()