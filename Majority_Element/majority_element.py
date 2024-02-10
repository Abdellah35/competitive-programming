class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        apears = len(nums)/3
        elemetsFound = []
        for key, value in counted.items():
            if value > apears:
                elemetsFound.append(key)
        
        return elemetsFound
