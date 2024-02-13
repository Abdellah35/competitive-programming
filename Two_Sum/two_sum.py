class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subDic = {}

        for i,num in enumerate(nums):
            value = target - num
            if value in subDic:
                return [i, subDic[value]]

            subDic[num] = i

        return []
