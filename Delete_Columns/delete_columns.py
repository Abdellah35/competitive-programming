class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0]) 
        toBedeleted = 0
        for i in range(cols):
            colChars = [strs[j][i] for j in range(rows)]
            if colChars != sorted(colChars):
                toBedeleted += 1
        
        return toBedeleted
