class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        good_int = 9999
        combined_lst = fronts + backs

        for x in combined_lst:
            if x not in same:
                good_int = min(good_int, x)
        
        if good_int < 9999:
            return good_int
        
        return 0
