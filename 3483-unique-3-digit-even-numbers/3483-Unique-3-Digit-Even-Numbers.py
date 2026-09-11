class Solution(object):
    def totalNumbers(self, digits):
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    
                    if i == j or j == k or i == k:
                        continue
                    
                    if digits[i] == 0:
                        continue
                    
                    if digits[k] % 2 != 0:
                        continue
                    
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)

        return len(ans)