N=input()
num=[]
result=''
for i in N:
    num.append(int(i))
for l in sorted(num,reverse=True):
    result+=str(l)
print(result)