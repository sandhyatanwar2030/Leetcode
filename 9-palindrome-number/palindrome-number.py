class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        l=list(s)
        return l==l[::-1]
        # if l == l[::-1]:
        #     return True
        # else:
        #     return False
        