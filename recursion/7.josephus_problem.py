def josephus_problem(n, k):
    if n == 1:
        return 0
    else:
        return (k+josephus_problem(n-1, k)) % n


if __name__ == "__main__":
    n = int(input("enter the number of persons: "))
    k = int(input("enter the position: "))
    print("the survivour's position is: ", josephus_problem(n, k))


==========================
class Solution:
    def jos(self,n,k):
        if n==1:
            return 0
        return (self.jos(n-1,k)+k)%n

    def findTheWinner(self, n: int, k: int) -> int:
        return self.jos(n,k)+1