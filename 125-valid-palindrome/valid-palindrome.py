class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=[]
        z=s.lower()
        for ch in z:

            if ch.isalnum():
                y.append(ch)
        return y==y[::-1]