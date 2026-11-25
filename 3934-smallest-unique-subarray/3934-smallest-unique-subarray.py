class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base = 911382323

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        # Build prefix hashes
        for i in range(n):
            pow1[i + 1] = pow1[i] * base % mod1
            pow2[i + 1] = pow2[i] * base % mod2

            pref1[i + 1] = (pref1[i] * base + nums[i]) % mod1
            pref2[i + 1] = (pref2[i] * base + nums[i]) % mod2

        def check(length):
            freq = {}

            for i in range(n - length + 1):
                j = i + length

                h1 = (pref1[j] - pref1[i] * pow1[length]) % mod1
                h2 = (pref2[j] - pref2[i] * pow2[length]) % mod2

                key = (h1, h2)

                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        # Binary Search
        left = 1
        right = n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans