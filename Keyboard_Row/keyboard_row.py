class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_dict = {char: 1 for char in 'qwertyuiop'}
        row_dict.update({char: 2 for char in 'asdfghjkl'})
        row_dict.update({char: 3 for char in 'zxcvbnm'})

        def can_construct(word):
            first_char = 0
            for char in word:
                if char in row_dict:
                    if first_char != row_dict[char] and first_char != 0:
                        return False
                    first_char = row_dict[char]
            return True
            
        canTypeds = []
        for word in words:
            if can_construct(word.lower()):
                canTypeds.append(word)

        return canTypeds
