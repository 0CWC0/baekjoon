def main():
    student_list=[i for i in range(1,31)]
    for check in range(28):
        n=int(input())
        student_list.remove(n)
    for value in student_list:
        print(value)
if __name__=='__main__':
    main()

