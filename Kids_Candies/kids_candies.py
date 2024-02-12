class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandi = max(candies)
        ansr = []
        for candy in candies:
            if candy + extraCandies >= maxCandi:
                ansr.append(True)
            else:
               ansr.append(False)

        return ansr 
