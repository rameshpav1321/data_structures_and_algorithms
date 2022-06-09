def hanoi_towers(discs, start_tow="A", dest_tow="C", aux_tow="B"):
    if discs == 1:
        print("Move disk %i from %s to %s" % (discs, start_tow, dest_tow))
    else:
        hanoi_towers(discs-1, start_tow, aux_tow, dest_tow)
        print("Move disk %i from %s to %s" % (discs, start_tow, dest_tow))
        hanoi_towers(discs-1, aux_tow, dest_tow, start_tow)


if __name__ == "__main__":
    discs = int(input("enter the discs count: "))
    hanoi_towers(discs)
