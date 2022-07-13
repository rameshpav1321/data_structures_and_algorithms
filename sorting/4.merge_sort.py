from merge_sorted import merge_sorted as merge


def merge_sort(lst, left, right):
    if right > left:
        mid = left+(right-left)//2
        # print(lst, left, right)
        merge_sort(lst, left, mid)
        merge_sort(lst, mid+1, right)
        # print(left, mid, right)
        merge(lst, left, mid, right)
        # print(lst)


if __name__ == "__main__":
    lst = [10, 5, 30, 15, 7, 30]
    merge_sort(lst, 0, 5)
    print(lst)
