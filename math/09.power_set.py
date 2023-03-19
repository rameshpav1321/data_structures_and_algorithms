def power_set(str, count, n):
    print(str, count, n)
    for i in range(count):
        for j in range(n):
            if((i & (1 << j)) != 0):
                print(str[j], end='')
        print('\n')


if __name__ == "__main__":
    str = input("enter any string: ")
    n = len(str)
    count = 2**n
    power_set(str, count, n)
