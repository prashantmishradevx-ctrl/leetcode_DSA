class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # value + original index
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # value ke according sort
        arr.sort()

        result = [0] * n

        i = 0

        while i < n:

            # current group
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # values of current group
            values = []

            # original indices of current group
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # indices ko sort karo
            indices.sort()

            # smallest values ko smallest indices par rakho
            for k in range(len(values)):
                result[indices[k]] = values[k]

            i = j + 1

        return result