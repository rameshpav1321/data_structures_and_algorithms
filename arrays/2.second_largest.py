def second_largest(lst):
    first_largest = 0
    second_largest = 1
    for i in range(1, len(lst)):
        if lst[i] > lst[first_largest]:
            second_largest = first_largest
            first_largest = i
        elif lst[second_largest] < lst[i] < lst[first_largest]:
            second_largest = i
    if lst[first_largest] != lst[second_largest]:
        return (lst[first_largest], first_largest), (lst[second_largest], second_largest)
    else:
        return("There is no second largest element")


print(second_largest([1,5,4,5]))

# if __name__ == "__main__":
#     lst = list(map(int, input("enter the values for the list: ").split()))
#     print(second_largest(lst))
