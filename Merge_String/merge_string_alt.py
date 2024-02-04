class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Identify the min and max length of the words
        minWord, maxWord = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        mergedString = ''
        min_index = len(minWord)

        for i in range(min_index):
            mergedString += word1[i]  + word2[i]

        return mergedString + maxWord[min_index:]
