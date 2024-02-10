class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums = []
        negetiveNums = []
        result = []
        for num in nums:
            if num >= 0:
                positiveNums.append(num)
            else:
                negetiveNums.append(num)
        for i in range(len(positiveNums)):
            result += [positiveNums[i], negetiveNums[i]]

        return result
