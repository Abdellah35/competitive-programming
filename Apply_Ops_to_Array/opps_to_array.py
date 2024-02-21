class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # apply the 1st rule
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        main_index = 0
        
        #Shifting all 0's to end
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[main_index], nums[i] = nums[i], nums[main_index]
                main_index += 1

        return nums
