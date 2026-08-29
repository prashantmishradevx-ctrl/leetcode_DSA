class Solution(object):
    def summaryRanges(self, nums):

        result = []

        if len(nums) == 0:
            return result

        start = nums[0]

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1] + 1:

                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))

                start = nums[i]

        # Last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result