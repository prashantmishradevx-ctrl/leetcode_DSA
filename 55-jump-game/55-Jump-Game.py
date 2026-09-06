class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        farthest = 0
        lst = n - 1

        for i in range(n):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= lst:
                return True

        return False