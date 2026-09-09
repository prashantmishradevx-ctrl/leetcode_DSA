class Solution(object):
    def findRepeatedDnaSequences(self, s):

        seen = set()
        result = set()

        for i in range(len(s) - 9):

            sequence = s[i:i+10]

            if sequence in seen:
                result.add(sequence)
            else:
                seen.add(sequence)

        return list(result)