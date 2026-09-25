class Solution(object):
    def backspaceCompare(self, s, t):
       
        n = len(s)
        chars = []
        for ch in s:
            if ch == "#":
                if chars:
                    chars.pop()
            else:
                chars.append(ch)
        news = "".join(chars)

        char = []
        for ch in t:
            if ch == "#":
                if char:
                    char.pop()
            else:
                char.append(ch)
        new  = "".join(char)
        if news == new:
            return True
        else:
            return False