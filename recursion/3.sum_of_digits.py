def sum_of_digits(n):
    if n == 0:
        return 0
    ld = n % 10
    return ld+sum_of_digits(n//10)


if __name__ == "__main__":
    n = int(input("enter a no: "))
    sum = sum_of_digits(n)
    print("sum of digits in the given no:", sum)
