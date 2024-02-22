class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_0 = 0
        count_1 = sum(nums)
        max_score = count_1
        result_indices = [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            else:
                count_1 -= 1

            current_score = count_1 + count_0

            if current_score == max_score:
                result_indices.append(i + 1)
            elif current_score > max_score:
                max_score = current_score
                result_indices = [i + 1]

        return result_indices
