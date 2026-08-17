class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        else:
            sum=1
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    sum=sum+i
                    # add a pair 
                    if i**2!=num:
                        sum=sum+(num//i)
            return sum==num

        