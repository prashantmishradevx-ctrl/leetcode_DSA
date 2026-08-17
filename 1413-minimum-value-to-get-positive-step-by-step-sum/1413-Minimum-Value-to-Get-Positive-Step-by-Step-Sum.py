class Solution(object):
    def minStartValue(self, nums):
        total = 0
        minimum = 0

        for i in nums:
            total += i

            if total < minimum:
                minimum = total

        return 1 - minimum