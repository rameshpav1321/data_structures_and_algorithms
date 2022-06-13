def parity(x):
    count = 0
    if x == 0:
        return 0
    else:
        while(x):
            x = x & (x-1)
            count += 1
        return count % 2


if __name__ == "__main__":
    x = int(input("enter a no. to find parity: "))
    print(parity(x))
