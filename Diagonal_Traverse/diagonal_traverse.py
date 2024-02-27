class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(mat), len(mat[0])
        direction = True 
        i, j = 0, 0

        for _ in range(rows * cols):
            result.append(mat[i][j])

            if direction:
                if j == cols - 1:
                    i += 1
                    direction = not direction
                elif i == 0:
                    j += 1
                    direction = not direction
                else:
                    i -= 1
                    j += 1
            else:
                if i == rows - 1:
                    j += 1
                    direction = not direction
                elif j == 0:
                    i += 1
                    direction = not direction
                else:
                    i += 1
                    j -= 1

        return result
