class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        comb = zip(*matrix)
        transposedList = list(map(list, comb))
        return transposedList
