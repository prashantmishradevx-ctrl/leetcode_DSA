class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        i = min(min_index, max_index)
        j = max(min_index, max_index)

        option1 = j + 1
        option2 = n - i
        option3 = (i + 1) + (n - j)

        return min(option1, option2, option3)