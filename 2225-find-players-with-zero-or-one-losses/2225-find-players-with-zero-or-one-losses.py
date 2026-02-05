class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer=[SortedSet(),SortedSet()]
        loser = defaultdict(int)

        players=set()
        winners=set()
        for w,l in matches:
            players.add(w)
            players.add(l)
            loser[l]+=1
            winners.add(w)
        for player in players:
            if player in winners and player not in loser:
                answer[0].add(player)
            if loser[player]==1:
                answer[1].add(player)
        answer=[list(answer[0]),list(answer[1])]
        return answer