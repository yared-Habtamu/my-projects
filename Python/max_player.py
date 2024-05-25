class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        one = 0
        two = 0
        ans = 0
        while one < len(players) and two < len(trainers):
            if players[one] <= trainers[two]:
                one +=1
                two +=1
                ans +=1
            else:
                two +=1
        return ans
