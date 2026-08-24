class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        ans = 0

        for i in range(n):

            if nums[i] % 2 == 0 and nums[i] <= threshold:

                j = i

                while j + 1 < n:
                    if nums[j + 1] <= threshold and nums[j + 1] % 2 != nums[j] % 2:
                        j += 1
                    else:
                        break

                ans = max(ans, j - i + 1)

        return ans