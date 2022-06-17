import math


def is_prime(x):
    print("func called")
    if x == 1:
        return False
    if x == 2 or x == 3:
        print("hi")
        return True
    for j in range(2, int(math.sqrt(x)+1)):
        if(x % j == 0):
            return False
    return True


if __name__ == "__main__":
    n = 450
    print("vikas")
    i = 2
    while n != 1:
        print("loop started")
        print(i)
        if(is_prime(i)):
            if(n % i == 0):
                print(i)
                n //= i
                i += 1
