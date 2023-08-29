def main():
    from string import ascii_lowercase
    S = input()
    alphabet_list = list(ascii_lowercase)
    for i in alphabet_list:
        if i in S:
            print(S.index(i), end=' ')
        else:
            print(-1, end=' ')


if __name__ == '__main__':
    main()
