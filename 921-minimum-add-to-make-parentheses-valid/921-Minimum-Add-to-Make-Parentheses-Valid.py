class Solution:
    def minAddToMakeValid(self, s):
        opening = 0
        ans = 0

        for ch in s:
            if ch == '(':
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    ans += 1

        ans += opening

        return ans