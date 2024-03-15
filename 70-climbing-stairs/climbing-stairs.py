class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        while n>1:
            t = a
            a += b
            b = t
            n-=1
        return a