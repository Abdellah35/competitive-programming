class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_dict = {i: i for i, char in enumerate(boxes) if char == '1'}
        result = []
        
        for i in range(len(boxes)):
            total_move = 0
            for j in index_dict.keys():
                if j != i:
                    total_move += abs(index_dict[j] - i)
            result.append(total_move)
        return result
