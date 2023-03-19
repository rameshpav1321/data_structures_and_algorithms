# def peak_element(lst, low, high):
#     while low <= high:
#         print("low:", low, "high:", high)
#         mid = (low+high)//2
#         if mid != 0 and mid != len(lst)-1 and lst[mid] >= lst[mid-1] and lst[mid] >= lst[mid+1]:
#             return mid
#         if mid == 0 and lst[mid] > lst[mid+1]:
#             return mid
#         if mid == 0 and lst[mid] < lst[mid+1]:
#             return
#         if mid == len(lst)-1 and lst[mid] > lst[mid-1]:
#             return mid
#         if mid == len(lst)-1 and lst[mid] < lst[mid-1]:
#             return
#         peak_element(lst, low, mid-1)
#         peak_element(lst, mid+1, high)
def peak_element(lst, low, high):
    while low <= high:
        mid = (low+high)//2
        if (lst[mid] >= lst[mid-1] or mid == 0) and (lst[mid] >= lst[mid+1] or mid == len(lst)-1):
            return mid
        if mid > 0 and lst[mid-1] >= lst[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1


if __name__ == "__main__":
    lst = [5, 20, 40, 30, 20, 50, 12]
    low = 0
    high = len(lst)-1
    print(peak_element(lst, low, high))
