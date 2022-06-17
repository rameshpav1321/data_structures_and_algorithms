x = int(input("enter the first no: "))
y = int(input("enter the second no: "))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(f"gcd of given no.'s is: {gcd(x,y)} ")
