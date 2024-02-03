class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Count all the items then define them in key(the number) values pair
        value_counts = Counter(nums)
        good_pairs = 0
        for count in value_counts.values():
            # If a number appears n times, then n * (n – 1) // 2 good pairs 
            # can be made with this number
            good_pairs += (count * (count -1) // 2)
        
        return good_pairs
