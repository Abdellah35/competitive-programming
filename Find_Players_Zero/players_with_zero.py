class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winers = set()
        losser = set()
        allLoses = set()
        for match in matches:

            
            if match[0] not in allLoses:
                winers.add(match[0])

            if match[1] not in allLoses:
                losser.add(match[1])
                if match[1] in winers:
                    winers.remove(match[1])
            elif match[1] in losser:
                losser.remove(match[1]) 
                if match[1] in winers:
                    winers.remove(match[1])

            allLoses.add(match[1])
            

        return [sorted(winers), sorted(losser)]
