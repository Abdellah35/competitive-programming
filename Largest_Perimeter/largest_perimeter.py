class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        def is_valid_triangle(a, b, c):
            return a + b > c and b + c > a and a + c > b

        nums.sort(reverse=True)
        length = len(nums)

        for i in range(length - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if is_valid_triangle(a, b, c):
                return a + b + c
        return 0
