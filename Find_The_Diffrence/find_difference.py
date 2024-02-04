class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = sorted(t)
        s = sorted(s)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        # incase the added letter sorted in the last index this condition will handle it
        if len(s) < len(t):
            return t[-1]

        return ''
