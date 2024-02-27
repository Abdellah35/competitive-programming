class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_ = 0
        for i in range(2,rows):
            for j in range(2,cols):
                sum_ = grid[i][j - 2] + grid[i][j - 1] + grid[i][j] + grid[i - 1][j - 1] + grid[i - 2][j - 2] + grid[i - 2][j - 1] + grid[i - 2][j]
                if sum_ > max_:
                    max_ = sum_
        
        return max_
