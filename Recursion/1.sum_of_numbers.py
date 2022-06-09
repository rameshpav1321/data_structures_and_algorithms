def sum_of_no(n):
    if n == 0:
        return 0
    return sum_of_no(n-1)+n


if __name__ == "__main__":
    n = int(input("enter the value for n: "))
    sum = sum_of_no(n)
    print(sum)
