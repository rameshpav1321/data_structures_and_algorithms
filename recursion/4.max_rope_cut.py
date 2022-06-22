def max_rope_cuts(len, p1, p2, p3):
    if len == 0:
        return 0
    elif len < 0:
        return -1
    else:
        res = max(max_rope_cuts(len-p1, p1, p2, p3),
                  max_rope_cuts(len-p2, p1, p2, p3),
                  max_rope_cuts(len-p3, p1, p2, p3))
        if res == -1:
            return -1
        return res+1


if __name__ == "__main__":
    len = int(input("enter the length of the rope: "))
    p1, p2, p3 = (input("enter three piece lenghts: ")).split()
    res = max_rope_cuts(len, int(p1), int(p2), int(p3))
    if res == 0 | -1:
        print("rope can't be split")
    else:
        print("rope can be split into {} pieces".format(res))
        print(f"rope can be split into {res} pieces")
