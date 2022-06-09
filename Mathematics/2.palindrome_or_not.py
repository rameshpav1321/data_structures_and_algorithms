x = int(input("enter a no. to check: "))
temp = x
rev = 0
while temp != 0:
    ld = temp % 10
    rev = 10*rev+ld
    temp //= 10
if x == rev:
    print("given no. is a palindrome")
else:
    print("not a palindrome")
