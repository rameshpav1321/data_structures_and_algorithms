# logic is find two consecutive bits that are different and swap them

def nearest_same_weight(x):
    bits_count = 3
    for i in range(bits_count-1):
        if ((1 & (x >> i)) != (1 & (x >> i+1))):
            print("hi")
            return x ^ (1 << i | 1 << i+1)
    raise ValueError('All bits are same')


if __name__ == "__main__":
    x = int(input("enter a number: "))
    print(nearest_same_weight(x))
