class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        toStr = ''.join(list(map(str, digits)))
        val = int(toStr) + 1
        return list(map(int, str(val)))
