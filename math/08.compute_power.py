def computer_power(x, n):
    print(x, n)
    res = 1
    while(n > 0):
        if(n % 2 != 0):
            res = res*x
        x = x**2
        n = n//2
    return res


if __name__ == "__main__":

    x = int(input("enter a value for x: "))
    n = int(input("enter a value for n: "))
    ans = computer_power(x, n)
    print(ans)
