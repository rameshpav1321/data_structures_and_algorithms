x = int(input("enter a number: "))
# temp = x
factorial = 1
# while temp != 0:
#     factorial *= temp
#     temp -= 1
for i in range(1, x+1):
    factorial = factorial*i
print(f"factorial of given no. is {factorial}")
count = 0
while(factorial % 10 == 0):
    count += 1
    factorial //= 10
print(f"trailing zeros in the given factorial are: {count}")
