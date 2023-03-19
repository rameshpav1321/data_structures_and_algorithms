import math

# def is_prime(x):
#     if x == 1:
#         return False
#     if x == 2 or x == 3:
#         return True
#     for j in range(2, int(math.sqrt(x)+1)):
#         if(x % j == 0):
#             return False
#     return True
# if __name__ == "__main__":
#     n = 450
#     i = 2
#     while n != 1:
#         if is_prime(i):
#             while n % i == 0:
#                 print(i)
#                 n //= i
#         i += 1


def prime_factors(n):
    if n <= 1:
        return
    for i in range(2, int(math.sqrt(n)+1)):
        while n % i == 0:
            print(i)
            n //= i
    if n > 1:
        print(n)


prime_factors(1)
