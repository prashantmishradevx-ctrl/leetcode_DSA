class Solution(object):
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            x = int(s[i:i+k])

            if x != 0 and num % x == 0:
                count += 1

        return count