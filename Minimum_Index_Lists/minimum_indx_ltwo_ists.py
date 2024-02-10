class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        allCommons = set(list1) & set(list2)
        indexValueDic = {word: list1.index(word) + list2.index(word)  for word in allCommons }

        minIndex = len(list1 + list2)
        result = []
        for key, value in indexValueDic.items():

            if value < minIndex:
                minIndex = value
                result = [key]
            elif value == minIndex:
                result.append(key)
    
        return result
