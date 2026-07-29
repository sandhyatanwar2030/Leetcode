class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return list(map(int, str(num)))
        # n=len(digits)-1
        # digits[n]=(digits[n]+1)
        # return digits

        