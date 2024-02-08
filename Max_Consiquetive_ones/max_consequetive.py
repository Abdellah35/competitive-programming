class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consiquetive1s = 0;
        current = 0;
        for num in nums:
            if num == 1:
                current += 1
                if current > max_consiquetive1s:
                    max_consiquetive1s = current
            else:
                current = 0
    
        return max_consiquetive1s;
