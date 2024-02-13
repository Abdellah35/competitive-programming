class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s = list(filter(lambda word: len(word) > 0, s.split(" ")))
        return ' '.join(s[::-1])
