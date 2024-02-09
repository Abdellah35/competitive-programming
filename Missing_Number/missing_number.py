class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dif = set(range(len(nums) +1)).difference(set(nums))
        return dif.pop()
