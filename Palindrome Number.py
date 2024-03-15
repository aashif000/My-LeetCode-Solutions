class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=str(x)
        x=str(i)
        if(i == i[::-1]):
            return True
        else:
            return False
