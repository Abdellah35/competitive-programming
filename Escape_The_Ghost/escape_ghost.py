class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        pac_man = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_moves = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            print(ghost_moves)
            if ghost_moves <= pac_man:
                return False
            
        return True
