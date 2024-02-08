class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # using a custome formula
        i = int((num - 3)/3)
        remaining = (num - 3)%3

        if remaining == 0:
            return [i, i + 1, i + 2]
        
        return []
