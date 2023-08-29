#2745
num=input().split()
print(int(num[0],int(num[1])))

#11005
import string
tmp=string.digits + string.ascii_uppercase
def convert(num, base):
    q,r=divmod(num,base)
    if q==0:
        return tmp[r]
    else :
        return convert(q,base)+tmp[r]
number=list(map(int,input().split())) #N,B
print(convert(number[0],number[1]))


