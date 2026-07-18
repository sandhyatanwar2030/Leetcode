class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        smallest = nums[0]
        largest = nums[-1]

        li = []

        for i in range(1, smallest + 1):
            if smallest % i == 0 and largest % i == 0:
                li.append(i)

        return li[-1]