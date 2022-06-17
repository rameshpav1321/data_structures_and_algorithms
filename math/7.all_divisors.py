import math


def all_divisors(x):
    for i in range(1, int(math.sqrt(x)+1)):
        if(x % i == 0):
            lst.append(i)
            temp = x//i
            if(temp != i):
                lst.append(temp)


if __name__ == "__main__":
    ip = int(input("enter a no: "))
    lst = []
    all_divisors(ip)
    lst.sort()
    print(lst)
