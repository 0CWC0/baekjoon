while True:
    length=list(map(int,input().split()))
    length.sort()
    if length==[0,0,0]:
        break
    if length[2]>=length[1]+length[0]:
        print('Invalid')
    elif length[0]==length[1]==length[2]:
        print('Equilateral')
    elif length[0]==length[1] or length[1]==length[2] or length[0]==length[2]:
        print('Isosceles')
    elif length[0]!=length[1]!=length[2]:
        print("Scalene")


