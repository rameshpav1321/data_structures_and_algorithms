def swap_bits(x, i, j):
    if (1 & (x >> i-1)) != (1 & (x >> j-1)):
        return x ^ (1 << i-1 | 1 << j-1)
    else:
        return x


if __name__ == "__main__":
    x, i, j = input("enter the no, bit positions to swap: ").split()
    print(swap_bits(int(x), int(i), int(j)))
