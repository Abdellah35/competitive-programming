class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        final_x = 0
        for operation in operations:
            if "++" in operation:
                final_x += 1
            else:
                final_x -= 1 
        
        return final_x
