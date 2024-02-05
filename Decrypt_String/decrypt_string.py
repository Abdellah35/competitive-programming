class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        first = 'abcdefghijklmnopqrstuvwxyz'

        formatted = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                formatted += first[int(s[i-2])*10 + int(s[i-1])  - 1]
                i -= 3
            else:
                formatted += first[int(s[i]) - 1]
                i -= 1
        
        return formatted[::-1]
