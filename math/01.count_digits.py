x = int(input("enter a number: "))
count = 0
while x != 0:
    x = x // 10
    count += 1
print(f"Digits in the given no: {count}")
