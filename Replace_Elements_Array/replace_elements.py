class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        nums_index = {num: index for index, num in enumerate(nums)}
        for operation in operations:
            if operation[0] in nums_index:
                nums[nums_index[operation[0]]] = operation[1]
                nums_index[operation[1]] = nums_index.pop(operation[0])

        return nums
