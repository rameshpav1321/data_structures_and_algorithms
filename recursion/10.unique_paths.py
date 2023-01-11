class Solution:
    my_dict={}
    def uniquePaths(self, m: int, n: int) -> int:
        if n==1 or m==1:
            return 1
        if (m,n) not in self.my_dict.keys():
            self.my_dict[(m,n)]=self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        return self.my_dict[(m,n)]