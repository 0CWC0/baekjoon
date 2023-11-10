n=int(input())
def star(num):
    if num==3:
        return ['***','* *','***']
    arr = star(num//3)
    stars = []
    for i in arr:
        stars.append(i* 3)
    for i in arr:
        stars.append(i+' '*(num//3)+i)
    for i in arr:
        stars.append(i * 3)

    return stars

print('\n'.join(star(n)))