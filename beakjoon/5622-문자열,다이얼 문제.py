def main():
    from string import ascii_uppercase
    sum=0
    numbers=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    s=list(input())
    for i in s:
        for k in numbers:
            if i in k:
                sum+=numbers.index(k) + 3
        sum+=numbers.index(i)
    """for i in s:
        if i in numbers[0:3]:
            sum+=3
        elif i in numbers[3:6]:
            sum+=4
        elif i in numbers[6:9]:
            sum+=5
        elif i in numbers[9:12]:
            sum+=6
        elif i in numbers[12:15]:
            sum+=7
        elif i in numbers[15:19]:
            sum+=8
        elif i in numbers[19:22]:
            sum+=9
        elif i in numbers[22:26]:
            sum+=10"""
    print(sum+len(s))

main()