class Solution(object):
    def subarraySum(self, nums, k):

        count = 0
        current_sum = 0

        prefix = {0: 1}

        for num in nums:

            current_sum += num

            if current_sum - k in prefix:
                count += prefix[current_sum - k]

            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1

        return count