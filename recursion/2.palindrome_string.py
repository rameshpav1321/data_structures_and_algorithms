from operator import truediv


def is_palindrome(str, strt, end):
    if strt >= end:
        return True
    return ((str[strt] == str[end]) & is_palindrome(str, strt+1, end-1))


if __name__ == "__main__":
    str = input("enter a string to check: ")
    strt = 0
    end = len(str)-1
    res = is_palindrome(str, strt, end)
    if res:
        print("given string is a palindrome")
    else:
        print("given string is not a palindrome")
