class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        row = len(img)
        col = len(img[0])

        ans = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                sum_ = 0
                count = 0
                for x in range(i-1, i+2, 1):
                    for y in range(j-1, j+2, 1):
                        if 0 <= x < row and 0 <= y < col:
                            sum_ += img[x][y]
                            count += 1
                ans[i][j] = sum_ // count
        return ans
