def swap(str, a, b):
    lst = list(str)
    lst[a], lst[b] = lst[b], lst[a]
    return ''.join(lst)


def permutations(str, i=0):
    if i == len(str)-1:
        print(str)
        return
    for j in range(i, len(str)):
        str = swap(str, i, j)
        permutations(str, i+1)
        str = swap(str, i, j)


if __name__ == "__main__":
    str = input("enter a string to find all permutations: ")
    permutations(str)
