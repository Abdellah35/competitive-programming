class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        higher = []
        medium = []
        for num in nums:
            if num > pivot:
                higher.append(num)
            elif num < pivot:
                lower.append(num)
            else:
                medium.append(num)

        return lower + medium + higher
