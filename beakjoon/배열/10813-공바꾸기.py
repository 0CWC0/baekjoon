def main():
    N, M = map(int, input().split())
    basket = list()
    n = 0
    while n < N:
        basket += [n + 1]
        n += 1
    temp = 0
    for m in range(M):
        i, j = map(int, input().split())
        temp = basket[i - 1]
        basket[i - 1] = basket[j - 1]
        basket[j - 1] = temp
    for elements in basket:
        print(elements, end=' ')


if __name__ == '__main__':
    main()

