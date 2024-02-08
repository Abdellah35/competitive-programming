class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        #Join both words array elemments and check if they are equal 
        return ''.join(word1) == ''.join(word2)
