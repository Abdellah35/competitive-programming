class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        current_index = 0

        #Iterate through friends based on k untill we left with 1 friends(last one)
        while len(friends) > 1:
            # using module of len of the remainig friends, will help to prevent the index out error
            current_index = (current_index + k - 1) % len(friends)            
            friends.pop(current_index)

        return friends[0]
